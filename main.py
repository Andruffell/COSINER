import time
import sys
import random
import pandas as pd
import numpy as np
from collections import Counter
import copy
import datasets
from datasets import ClassLabel, load_dataset, load_metric, Dataset
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
from transformers.trainer_utils import get_last_checkpoint
from transformers.utils import check_min_version
from transformers.utils.versions import require_version
from transformers import AutoModelForTokenClassification, AutoTokenizer
import utils



if __name__ == '__main__':
    args = utils.parse_args(sys.argv[1:])
    # Variabili e randomicità
    #os.environ["WANDB_DISABLED"] = "true"
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

    #Download dei dataset (train, validation, test) features: ['id', 'tokens', 'ner_tags']
    raw_datasets = load_dataset("drAbreu/BLURB", ds_config)
    print(raw_datasets)
    column_names = raw_datasets["train"].column_names
    features = raw_datasets["train"].features
    label_list = features['ner_tags'].feature.names
    print("Nomi colonne:", column_names)
    print("Tipi features:", features)
    print("Label list:", label_list)

    print(raw_datasets['train'][1727])
    samples_num = random.sample(range(len(raw_datasets['train'])), dataset_length)
    training_set = raw_datasets['train'].select(samples_num) if dataset_length > 0 else raw_datasets['train']

    #small_test_set = utils.extract_small_set(ontology, raw_datasets['test'])
    #print(small_test_set)

    label_list = features['ner_tags'].feature.names
    print("Labels: ", label_list)
    label_to_id = {i: i for i in range(len(label_list))}

    # tokenizer = AutoTokenizer.from_pretrained(
    #   model_type,
    #   use_fast=True, 
    #   padding="max_length",
    #   truncation=True,
    #   add_prefix_space=True
    # )

    b_to_i_label = []
    for idx, label in enumerate(label_list):
        if label.startswith("B-") and label.replace("B-", "I-") in label_list:
            b_to_i_label.append(label_list.index(label.replace("B-", "I-")))
        else:
            b_to_i_label.append(idx)

    tokenizer = AutoTokenizer.from_pretrained(model_type)
    pipe = pipeline('feature-extraction', model=model_type, tokenizer=tokenizer)

    ontology = utils.ontologyGeneration(training_set)
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

    starting_time = time.time()
    similarityList = utils.cosine_similarity(embeddings, examples_per_row, reverse)
    print(similarityList)
'''
counterfactualExamples = []
appendingIndex = len(training_set)

eligible_rows = 0
for row_check in training_set:
    if row_check['ner_tags'].count(1)>0:
        eligible_rows +=1
print(len(v_concept))
mid_time = time.time()
print(mid_time-starting_time)

for row in training_set:
    if row['ner_tags'].count(1)>0:
        id = copy.deepcopy(row['id'])
        tokens = copy.deepcopy(row['tokens'])
        ner_tags = copy.deepcopy(row['ner_tags'])
        for j in range(numero_esempi_per_row):
            indexList = []
            newIndexList = []
            oldDiseases = []
            for idx, (token, ner_tag) in enumerate(zip(tokens, ner_tags)):
                if ner_tag == 1:
                    oldDisease = []
                    oldDisease.append(token)
                    newIndexList = []
                    newIndexList.append(tokens.index(token))
                    if len(tokens)-1 == idx:
                        oldDiseases.append(oldDisease)
                        oldDisease = [] 
                        indexList.append(newIndexList)
                        newIndexList = []
                elif ner_tag == 2:
                    oldDisease.append(token)
                    newIndexList.append(tokens.index(token))
                    if len(tokens)-1 == idx:
                        oldDiseases.append(oldDisease)
                        oldDisease = [] 
                        indexList.append(newIndexList)
                        newIndexList = []
                else:
                    if newIndexList != []:
                        indexList.append(newIndexList)
                        oldDiseases.append(oldDisease)
                        oldDisease = []
                        newIndexList = []     
            similarityValue = []
            for idx, i in enumerate(range(len(indexList))):
                disease = indexList[len(indexList)-1-i]
                diseaseStart = disease[0]

                for word in disease:
                    tokens.pop(diseaseStart)
                    ner_tags.pop(diseaseStart)

                oldDisease = " ".join(oldDiseases[idx])
                newDisease = [list(similarityList[oldDisease])[j]]
                similarityValue.append(list(similarityList[oldDisease].values())[j])
                for idx, word in enumerate(newDisease):
                    tokens.insert(diseaseStart+idx, word)
                    if idx == 0:
                        ner_tags.insert(diseaseStart+idx, 1)
                    else:
                        ner_tags.insert(diseaseStart+idx, 2)

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
#print(counterfactual_set)
end_time=time.time()

print("Execution time: {}".format(round(end_time-mid_time, 10)))

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

eval_dataset = raw_datasets['validation'].map(
                tokenize_and_align_labels,
                batched=True,
                desc="Running tokenizer on validation dataset",
            ).remove_columns(['ner_tags', 'id', 'tokens'])
predict_dataset = raw_datasets['test'].map(
                tokenize_and_align_labels,
                batched=True,
                desc="Running tokenizer on prediction dataset",
            ).remove_columns(['ner_tags', 'id', 'tokens'])
small_predict_dataset = small_test_set.map(
                tokenize_and_align_labels,
                batched=True,
                desc="Running tokenizer on prediction dataset",
            ).remove_columns(['ner_tags', 'id', 'tokens'])


data_collator = DataCollatorForTokenClassification(tokenizer)
metric = load_metric("seqeval")

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
eval_metrics = []
test_metrics = []
small_test_metrics = []

trainer = Trainer(
        model=model,
        train_dataset= datasets.concatenate_datasets([train_dataset,counterfactual_set_tokenized]),
        eval_dataset=eval_dataset,
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
        args = TrainingArguments(num_train_epochs=startingEpochs, output_dir = str("./output"), evaluation_strategy="epoch", save_strategy="no")
)       
trainer.add_callback(CustomCallback(eval_metrics)) 

train_result = trainer.train()
print(train_result)
metrics = train_result.metrics
train_metrics.append(train_result.metrics)

max_train_samples = len(train_dataset)
metrics["train_samples"] = min(max_train_samples, len(train_dataset))

print(eval_metrics)
raw_predictions, labels, metricTest = trainer.predict(predict_dataset, metric_key_prefix="test")
test_metrics.append(metricTest)
raw_predictions, labels, metricSmallTest = trainer.predict(small_predict_dataset, metric_key_prefix="small_test")
small_test_metrics.append(metricSmallTest)

print(eval_metrics)
train_keys = list(train_metrics[0].keys())
eval_keys = list(eval_metrics[0].keys())
test_keys = list(test_metrics[0].keys())
small_test_keys = list(small_test_metrics[0].keys())
#print(train_keys, eval_keys, test_keys, small_test_keys)
print('\n')
train_metrics_byKeys = {}
for key in train_keys:
    train_metrics_byKeys[key] = []

for metric in train_metrics:
    for key in train_keys:
        train_metrics_byKeys[key].append(metric[key])
print(train_metrics_byKeys)

eval_metrics_byKeys = {}
for key in eval_keys:
    eval_metrics_byKeys[key] = []

for metric in eval_metrics:
    for key in eval_keys:
        try:
            eval_metrics_byKeys[key].append(metric[key])
        except:
            continue
print(eval_metrics_byKeys)

test_metrics_byKeys = {}
for key in test_keys:
    test_metrics_byKeys[key] = []

for metric in test_metrics:
    for key in test_keys:
        test_metrics_byKeys[key].append(metric[key])
print(test_metrics_byKeys)

small_test_metrics_byKeys = {}
for key in small_test_keys:
    small_test_metrics_byKeys[key] = []

for metric in small_test_metrics:
    for key in small_test_keys:
        small_test_metrics_byKeys[key].append(metric[key])
print(small_test_metrics_byKeys)

print('\n')
print(eval_metrics_byKeys)
train_df=pd.DataFrame(train_metrics_byKeys)
eval_df=pd.DataFrame(eval_metrics_byKeys)
test_df=pd.DataFrame(test_metrics_byKeys)
small_test_df=pd.DataFrame(small_test_metrics_byKeys)

with pd.ExcelWriter(xlsxoutput) as writer:  
    train_df.to_excel(writer, sheet_name='train')
    eval_df.to_excel(writer, sheet_name='eval')
    test_df.to_excel(writer, sheet_name='test')
    small_test_df.to_excel(writer, sheet_name='small_test')
'''
