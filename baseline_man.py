import time
import sys
import random
import pandas as pd
import numpy as np
import datasets
from datasets import load_dataset
import torch
import evaluate
import transformers
import  argparse
from transformers import (
    AutoConfig,
    AutoModelForTokenClassification,
    AutoTokenizer,
    DataCollatorForTokenClassification,
    Trainer,
    TrainingArguments,
)
from transformers import AutoModelForTokenClassification, AutoTokenizer
import baseline
import nltk

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-model', default="dmis-lab/biobert-v1.1", type=str, help="Model name") #biobert  and bert
    parser.add_argument('-epochs', default=5, type=int, help='Number of training epochs')
    parser.add_argument('-seed', default=100, type=int, help="Seed for randomicity")
    parser.add_argument('-dataset', default='NCBI-disease-IOB', type=str, choices=["NCBI-disease-IOB", "BC5CDR-chem-IOB", "BC2GM-IOB"], help="\nNCBI-disease-IOB: diseases dataset,\nBC5CDR-chem-IOB: chemical dataset,\nBC2GM-IOB: genetic dataset")
    parser.add_argument('-length', default=108, type=int, help="Dataset length reduction")
    parser.add_argument('-baseline', default='none', choices=['none', 'lwtr', 'mr', 'sr', 'style_ner', 'melm'])
    args = parser.parse_args(argv)
    return args

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
                if word_idx is None:
                    label_ids.append(-100)
                elif word_idx != previous_word_idx:
                    label_ids.append(label_to_id[label[word_idx]])
                else:
                    label_ids.append(b_to_i_label[label_to_id[label[word_idx]]])

                previous_word_idx = word_idx

            labels.append(label_ids)
        tokenized_inputs["labels"] = labels
        return tokenized_inputs

def compute_metrics(p):
        predictions, labels = p
        predictions = np.argmax(predictions, axis=2)

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
    args = parse_args(sys.argv[1:])
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(device)

    print(args)
    model_type = args.model
    startingEpochs = args.epochs
    seed = args.seed
    ds_config = args.dataset
    dataset_length = args.length
    xlsxoutput = "{}_{}_{}.xlsx".format(args.baseline, ds_config, str(seed))
    
    transformers.set_seed(seed)

    raw_datasets = load_dataset("drAbreu/BLURB", ds_config)
    print(raw_datasets)
    column_names = raw_datasets["train"].column_names
    features = raw_datasets["train"].features
    label_list = features['ner_tags'].feature.names
    print("Label list:", label_list)

    samples_num = random.sample(range(len(raw_datasets['train'])), dataset_length)
    training_set = raw_datasets['train'].select(samples_num) if dataset_length > 0 else raw_datasets['train']
    training_sample = training_set[4]
    label_to_id = {i: i for i in range(len(label_list))}

    b_to_i_label = []
    for idx, label in enumerate(label_list):
        if label.startswith("B-") and label.replace("B-", "I-") in label_list:
            b_to_i_label.append(label_list.index(label.replace("B-", "I-")))
        else:
            b_to_i_label.append(idx)
    
    tokenizer = AutoTokenizer.from_pretrained(model_type, padding=True)
    counterfactual_set = None

    if args.baseline == 'lwtr':
        counterfactual_set = baseline.lwt_replacement(training_set, label_list)
    elif args.baseline == 'mr':
        lexicon = baseline.lexiconGeneration(training_set, label_list)
        counterfactual_set = baseline.mention_replacement(training_set, lexicon, label_list)
    elif args.baseline == 'sr':
        nltk.download('wordnet')
        counterfactual_set = baseline.syn_with_word_net(training_set, label_list)
    elif args.baseline == 'style_ner':
        pass
    elif args.baseline == 'melm':
        pass
    else:
        pass

    print("COUNTERFACTUAL SET:", counterfactual_set)
    
    train_dataset = training_set.map(
                    tokenize_and_align_labels,
                    batched=True,
                    desc="Running tokenizer on train dataset"
    ).remove_columns(['ner_tags', 'id', 'tokens'])

    if counterfactual_set != None:
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

    final_train_dataset = datasets.concatenate_datasets([train_dataset,counterfactual_set_tokenized])  if counterfactual_set != None else train_dataset
    print(final_train_dataset)
    trainer = Trainer(
            model=model.to(device),
            train_dataset= final_train_dataset,
            tokenizer=tokenizer,
            data_collator=data_collator,
            compute_metrics=compute_metrics,
            args = TrainingArguments(optim="adamw_torch", num_train_epochs=startingEpochs, output_dir = str("./output"), evaluation_strategy="no", save_strategy="no", do_eval=False)
    )       

    train_result = trainer.train()
    metrics = train_result.metrics
    train_metrics.append(train_result.metrics)

    max_train_samples = len(train_dataset)
    metrics["train_samples"] = min(max_train_samples, len(train_dataset))

    raw_predictions, labels, metricTest = trainer.predict(predict_dataset, metric_key_prefix="test")
    test_metrics.append(metricTest)

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