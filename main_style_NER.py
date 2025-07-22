import sys
import utils
import random

import numpy as np
import pandas as pd
import torch
import evaluate

from datasets import Dataset
from datasets import load_from_disk, Sequence
from transformers import AutoTokenizer
from transformers import DataCollatorForTokenClassification
from transformers import AutoConfig,AutoModelForTokenClassification, TrainingArguments, Trainer, enable_full_determinism

from datasets import concatenate_datasets
import os
import time

from style_NER.sner_augmenter import SNER_Augmenter

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
    # Unpack nested dictionaries
    final_results = {}
    for key, value in results.items():
        if isinstance(value, dict):
            for n, v in value.items():
                final_results[f"{key}_{n}"] = v
        else:
            final_results[key] = value
    return final_results

if __name__ == '__main__':
    ###############
    #### SETUP ####
    ###############

    args = utils.parse_args(sys.argv[1:])
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    print(device)
    print(args)
    enable_full_determinism(args.seed)
    dataset_name = args.dataset.split('/')[-1].split('.')[0]

    if args.dataset == "data/ncbi.hf":
        source_dataset = "data/bc5cdr_disease.hf"
        source_name = "bc5cdr_disease"
        target_name = "ncbi"
    elif args.dataset == "data/bc5cdr.hf":
        source_dataset = "data/chemdner.hf"
        source_name = "chemdner"
        target_name = "bc5cdr"
    elif args.dataset == "data/bc2gm.hf":
        source_dataset = "data/jnlpba.hf"
        source_name = "jnlpba"
        target_name = "bc2gm"
    else:
        print("No source dataset found")
        sys.exit(0)
    
    print(f"[style_NER] transfer from {source_name} to {target_name}")
    xlsxoutput = f"{dataset_name}_{str(args.length)}_{str(args.seed)}.xlsx"
    metric = evaluate.load("seqeval")

    id2label = {0: 'O', 1: 'B', 2: 'I'}
    label2id = {v: k for k, v in id2label.items()}
    label_list = list(label2id.keys())

    b_to_i_label = []
    for idx, label in enumerate(label_list):
        if label.startswith("B-") and label.replace("B-", "I-") in label_list:
            b_to_i_label.append(label_list.index(label.replace("B-", "I-")))
        else:
            b_to_i_label.append(idx)

    source_dataset = load_from_disk(source_dataset)
    dataset = load_from_disk(args.dataset)
    features = dataset["train"].features
    samples_num = random.sample(range(len(dataset['train'])), args.length)
    dataset['train'] = dataset['train'].select(samples_num) if args.length > 0 else dataset['train']
    print(dataset['train'])

    tokenizer = AutoTokenizer.from_pretrained(args.model, 
                                              local_files_only=True, 
                                              padding=True, 
                                              num_labels=len(label_list))
    
    data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)

    model = AutoModelForTokenClassification.from_pretrained(args.model,
                                                        cache_dir=None,
                                                        num_labels=len(label_list), 
                                                        id2label=id2label, 
                                                        label2id=label2id,
                                                        token=None,
                                                        )
    model.to(device)

    config = AutoConfig.from_pretrained(
        args.model,
        num_labels=len(label_list),
        label2id=label2id,
        id2label={i: l for l, i in label2id.items()},
        finetuning_task='ner',
        cache_dir=None,
        revision="main",
    )

    training_args = TrainingArguments(
                                optim="adamw_torch",
                                num_train_epochs=args.epochs,
                                output_dir = str("./output"),
                                evaluation_strategy="no",
                                save_strategy="no",
                                do_eval=False,
                                seed=args.seed,
                                full_determinism=True)

    metric = evaluate.load("seqeval")


    # Splitting in training and validation
    splitted_target = dataset['train'].train_test_split(test_size=0.5)

    # Tokenization
    tokenized_dataset = dataset.map(utils.tokenize_and_align_labels,
                        batched=True,
                        desc="Running tokenizer on train dataset", 
                        fn_kwargs={"tokenizer": tokenizer, "b_to_i_label": b_to_i_label}
        )

    # Generation of the augmented pool
    os.chdir('style_NER')
    start_time = time.time()
    data_augmenter = SNER_Augmenter(args.seed, source_dataset, splitted_target, source_name, target_name)
    data_augmenter.fit()
    augmented_pool = data_augmenter.augment_dataset()
    augmentation_time = time.time() - start_time
    os.chdir("..")
    print("New sentences: ", len(augmented_pool))

    augmented_pool = Dataset.from_pandas(pd.DataFrame.from_dict(augmented_pool))
    tokenized_augmented_pool = augmented_pool.map(utils.tokenize_and_align_labels,
                        batched=True,
                        desc="Running tokenizer on augmented dataset", 
                        fn_kwargs={"tokenizer": tokenizer, "b_to_i_label": b_to_i_label}
        )
    tokenized_augmented_pool = tokenized_augmented_pool.cast_column("ner_tags", Sequence(feature=tokenized_dataset['train'].features['ner_tags'].feature))

    ##################
    #### TRAINING ####
    ##################

    # Loading Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=concatenate_datasets([tokenized_dataset['train'], tokenized_augmented_pool]).shuffle(seed=args.seed),
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )

    train_metrics = []
    test_metrics = []
    train_result = trainer.train()

    metrics = train_result.metrics
    train_metrics.append(train_result.metrics)

    max_train_samples = len(tokenized_dataset['train'])
    metrics["train_samples"] = min(max_train_samples, len(tokenized_dataset['train']))

    metricTest = trainer.evaluate(tokenized_dataset['test'], metric_key_prefix="test")
    metricTest["AUGMENTATION_TIME"] = augmentation_time
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

    with pd.ExcelWriter(f"results/style_NER/{xlsxoutput}") as writer:  
        train_df.to_excel(writer, sheet_name='train')
        test_df.to_excel(writer, sheet_name='test')

