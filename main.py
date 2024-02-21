import time
import sys
import random
import pandas as pd
import numpy as np
from collections import Counter
import copy
import datasets
from datasets import ClassLabel, load_dataset, Dataset
import evaluate
import transformers
from transformers import (
    AutoConfig,
    AutoModelForTokenClassification,
    AutoTokenizer,
    DataCollatorForTokenClassification,
    Trainer,
    pipeline,
    TrainingArguments,
)
from transformers import AutoModelForTokenClassification, AutoTokenizer
import utils

def tokenize_and_align_labels(examples):
        tokenized_inputs = tokenizer(
            examples['tokens'],
            padding="max_length",
            truncation=True,
            max_length=512,
            is_split_into_words=True,
        )
        labels = []
        for i, label in enumerate(examples["ner_tags"]):
            word_ids = tokenized_inputs.word_ids(batch_index=i)
            previous_word_idx = None
            label_ids = []
            for word_idx in word_ids:
                # Special tokens have a word id that is None. We set the label to -100 so they are automatically
                # ignored in the loss function.
                if word_idx is None:
                    label_ids.append(-100)
                # We set the label for the first token of each word.
                elif word_idx != previous_word_idx:
                    label_ids.append(label_to_id[label[word_idx]])
                # For the other tokens in a word, we set the label to either the current label or -100, depending on
                # the label_all_tokens flag.
                else:
                    label_ids.append(b_to_i_label[label_to_id[label[word_idx]]])

                previous_word_idx = word_idx

            labels.append(label_ids)
        tokenized_inputs["labels"] = labels
        return tokenized_inputs

def compute_metrics(p):
        predictions, labels = p
        predictions = np.argmax(predictions, axis=2)

        # Remove ignored index (special tokens)
        true_predictions = [
            [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
            for prediction, label in zip(predictions, labels)
        ]
        true_labels = [
            [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
            for prediction, label in zip(predictions, labels)
        ]
        results = metric.compute(predictions=true_predictions, references=true_labels)
        final_results = {}
        for key, value in results.items():
            if isinstance(value, dict):
                for n, v in value.items():
                    final_results[f"{key}_{n}"] = v
            else:
                final_results[key] = value
        return final_results

if __name__ == '__main__':
    args = utils.parse_args(sys.argv[1:])

    print(args)
    model_type = args.model
    startingEpochs = args.epochs
    seed = args.seed
    ds_config = args.dataset
    dataset_length = args.length
    reverse = args.reverse
    budget = args.budget
    examples_per_row = args.exr
    xlsxoutput = "{}_{}.xlsx".format(ds_config, str(seed))
    
    transformers.set_seed(seed)

    raw_datasets = load_dataset("drAbreu/BLURB", ds_config)
    print(raw_datasets)
    column_names = raw_datasets["train"].column_names
    features = raw_datasets["train"].features
    label_list = features['ner_tags'].feature.names
    print("Label list:", label_list)

    samples_num = random.sample(range(len(raw_datasets['train'])), dataset_length)
    training_set = raw_datasets['train'].select(samples_num) if dataset_length > 0 else raw_datasets['train']

    label_to_id = {i: i for i in range(len(label_list))}

    b_to_i_label = []
    for idx, label in enumerate(label_list):
        if label.startswith("B-") and label.replace("B-", "I-") in label_list:
            b_to_i_label.append(label_list.index(label.replace("B-", "I-")))
        else:
            b_to_i_label.append(idx)

    tokenizer = AutoTokenizer.from_pretrained(model_type, padding=True)
    pipe = pipeline('feature-extraction', model=model_type, tokenizer=tokenizer)

    ontology = utils.lexiconGeneration(training_set)
    embeddings = {}

    for entity, info in ontology.items():
        joinedEntity = ' '.join(entity)
        
        c_concept = info[0]
        lr = 1/c_concept    
        sentences = [sentence for sentence in info[1]]
        
        object_set = []
        c = dict(Counter(sentences))
        for s in c.keys():
            object_set.append((training_set.filter(lambda example: int(example['id']) in [int(s)])[0], c[s]))
            
        v_concept = 0
        for sentence in object_set:
            joinedSentence = ' '.join(sentence[0]['tokens'])
            tokenizedSentence = tokenizer(joinedSentence)['input_ids']
            tokenizedEntity = tokenizer(joinedEntity)['input_ids'][1:-1]

            for idx in range(sentence[1]):
                looking_index = 0
                start = 0
                end = 0
                for starting_index, token in enumerate(tokenizedSentence):
                    if token == tokenizedEntity[0]:
                        if looking_index == idx:
                            looking_list = tokenizedSentence[starting_index:starting_index+len(tokenizedEntity)]
                            if looking_list == tokenizedEntity:
                                start = starting_index
                                end = starting_index+len(tokenizedEntity)
                                looking_index += 1
                        else:
                            looking_index += 1

                words_embeddings = pipe(joinedSentence)
                v_context = np.array(words_embeddings[0])[start:end].mean(axis=0)

                if idx == 0:
                    v_concept = utils.update_v_concept(v_context, v_context, c_concept)
                else:
                    v_concept = utils.update_v_concept(v_concept, v_context, c_concept)       
        embeddings[' '.join(entity)] = v_concept

    similarityList = utils.cosine_similarity(embeddings, examples_per_row, reverse)

    counterfactualExamples = []
    appendingIndex = len(training_set)

    eligible_rows = 0
    for row_check in training_set:
        if row_check['ner_tags'].count(1)>0:
            eligible_rows +=1
    print(len(v_concept))

    for row in training_set:
        if row['ner_tags'].count(1)>0:
            id = copy.deepcopy(row['id'])
            tokens = copy.deepcopy(row['tokens'])
            ner_tags = copy.deepcopy(row['ner_tags'])
            for j in range(examples_per_row):
                indexList = []
                newIndexList = []
                oldEntities = []
                for idx, (token, ner_tag) in enumerate(zip(tokens, ner_tags)):
                    if ner_tag == 1:
                        oldEntity = []
                        oldEntity.append(token)
                        newIndexList = []
                        newIndexList.append(tokens.index(token))
                        if len(tokens)-1 == idx:
                            oldEntities.append(oldEntity)
                            oldEntity = [] 
                            indexList.append(newIndexList)
                            newIndexList = []
                    elif ner_tag == 2:
                        oldEntity.append(token)
                        newIndexList.append(tokens.index(token))
                        if len(tokens)-1 == idx:
                            oldEntities.append(oldEntity)
                            oldEntity = [] 
                            indexList.append(newIndexList)
                            newIndexList = []
                    else:
                        if newIndexList != []:
                            indexList.append(newIndexList)
                            oldEntities.append(oldEntity)
                            oldEntity = []
                            newIndexList = []     
                similarityValue = []
                for idx, i in enumerate(range(len(indexList))):
                    entity = indexList[len(indexList)-1-i]
                    entityStart = entity[0]

                    for word in entity:
                        tokens.pop(entityStart)
                        ner_tags.pop(entityStart)

                    oldEntity = " ".join(oldEntities[idx])
                    newDisease = [list(similarityList[oldEntity])[j]]
                    similarityValue.append(list(similarityList[oldEntity].values())[j])
                    for idx, word in enumerate(newDisease):
                        tokens.insert(entityStart+idx, word)
                        if idx == 0:
                            ner_tags.insert(entityStart+idx, 1)
                        else:
                            ner_tags.insert(entityStart+idx, 2)

                newExample = copy.deepcopy([str(appendingIndex), tokens, ner_tags])
                finalValue = np.mean(similarityValue)
                counterfactualExamples.append((newExample, finalValue))
                appendingIndex += 1
                id = copy.deepcopy(row['id'])
                tokens = copy.deepcopy(row['tokens'])
                ner_tags = copy.deepcopy(row['ner_tags'])

    budget = len(counterfactualExamples) if budget == 0 or budget > len(counterfactualExamples) else budget
    counterfactualExamples = sorted(counterfactualExamples, key=lambda item: item[1], reverse=not reverse)[0: budget]
    counterfactualExamples = list(zip(*counterfactualExamples))[0]
    counterfactual_set = Dataset.from_pandas(pd.DataFrame(counterfactualExamples, columns=["id", "tokens", "ner_tags"]))
    new_features = counterfactual_set.features.copy()
    new_features["ner_tags"] = datasets.features.features.Sequence(ClassLabel(names=label_list))
    counterfactual_set = counterfactual_set.cast(new_features)

    train_dataset = training_set.map(
                    tokenize_and_align_labels,
                    batched=True,
                    desc="Running tokenizer on train dataset"
    ).remove_columns(['ner_tags', 'id', 'tokens'])

    counterfactual_set_tokenized = counterfactual_set.map(
                    tokenize_and_align_labels,
                    batched=True,
                    desc="Running tokenizer on validation dataset",
                ).remove_columns(['ner_tags', 'id', 'tokens'])

    predict_dataset = raw_datasets['test'].map(
                    tokenize_and_align_labels,
                    batched=True,
                    desc="Running tokenizer on prediction dataset",
                ).remove_columns(['ner_tags', 'id', 'tokens'])

    data_collator = DataCollatorForTokenClassification(tokenizer)
    metric = evaluate.load("seqeval")

    config = AutoConfig.from_pretrained(
            model_type,
            num_labels=len(label_list),
            label2id=label_to_id,
            id2label={i: l for l, i in label_to_id.items()},
            finetuning_task='ner',
            cache_dir=None,
            revision="main",
            use_auth_token=False,
        )

    model = AutoModelForTokenClassification.from_pretrained(
            model_type,
            from_tf=bool(".ckpt" in model_type),
            config=config,
            cache_dir=None,
            revision="main",
            use_auth_token=False,
        )

    train_metrics = []
    test_metrics = []

    trainer = Trainer(
            model=model,
            train_dataset= datasets.concatenate_datasets([train_dataset,counterfactual_set_tokenized]),
            tokenizer=tokenizer,
            data_collator=data_collator,
            compute_metrics=compute_metrics,
            args = TrainingArguments(optim="adamw_torch", num_train_epochs=startingEpochs, output_dir = str("./output"), evaluation_strategy="no", save_strategy="no", do_eval=False)
    )       

    train_result = trainer.train()
    print(train_result)
    metrics = train_result.metrics
    train_metrics.append(train_result.metrics)

    max_train_samples = len(train_dataset)
    metrics["train_samples"] = min(max_train_samples, len(train_dataset))

    raw_predictions, labels, metricTest = trainer.predict(predict_dataset, metric_key_prefix="test")
    test_metrics.append(metricTest)
    print(test_metrics)


    train_keys = list(train_metrics[0].keys())
    test_keys = list(test_metrics[0].keys())
    train_metrics_byKeys = {}
    for key in train_keys:
        train_metrics_byKeys[key] = []

    for metric in train_metrics:
        for key in train_keys:
            train_metrics_byKeys[key].append(metric[key])
    print(train_metrics_byKeys)

    test_metrics_byKeys = {}
    for key in test_keys:
        test_metrics_byKeys[key] = []

    for metric in test_metrics:
        for key in test_keys:
            test_metrics_byKeys[key].append(metric[key])
    print(test_metrics_byKeys)

    train_df=pd.DataFrame(train_metrics_byKeys)
    test_df=pd.DataFrame(test_metrics_byKeys)

    with pd.ExcelWriter(xlsxoutput) as writer:  
        train_df.to_excel(writer, sheet_name='train')
        test_df.to_excel(writer, sheet_name='test')
