import sys
import time

import pandas as pd
import torch
import evaluate
import random

from datasets import load_from_disk, concatenate_datasets
from transformers import (AutoModelForTokenClassification, 
                          Trainer, 
                          AutoTokenizer, 
                          DataCollatorForTokenClassification, 
                          TrainingArguments, 
                          enable_full_determinism)

from baseline import Baseline
import utils

if __name__ == '__main__':
    args = utils.parse_args(sys.argv[1:])
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    print(device)
    print(args)

    baseline = args.baseline if args.baseline != None else "mr"

    enable_full_determinism(args.seed)
    dataset_name = args.dataset.split('/')[-1].split('.')[0]

    xlsxoutput = f"{dataset_name}_{baseline}_{str(args.length)}_{str(args.exr)}_{str(args.budget)}_{str(args.reverse)}_{str(args.seed)}.xlsx"
    metric = evaluate.load("seqeval")

    dataset = load_from_disk(args.dataset)
    features = dataset["train"].features
    label_list = features['ner_tags'].feature.names
    id2label = {i: label_list[i] for i in range(len(label_list))}
    label2id = {label_list[i]: i for i in range(len(label_list))}

    b_to_i_label = []
    for idx, label in enumerate(label_list):
        if label.startswith("B-") and label.replace("B-", "I-") in label_list:
            b_to_i_label.append(label_list.index(label.replace("B-", "I-")))
        else:
            b_to_i_label.append(idx)

    # Dataset sampling for few-shot scenarios
    samples_num = random.sample(range(len(dataset['train'])), args.length)
    dataset['train'] = dataset['train'].select(samples_num) if args.length > 0 else dataset['train']
    print(dataset['train'])

    start_time = time.time()
    print(args.baseline)
    counterfactual_set = Baseline(args.baseline, dataset['train'], label_list).generate_counterfactual_set()
    augmentation_time = time.time() - start_time

    model = AutoModelForTokenClassification.from_pretrained(
                                                        args.model,
                                                        cache_dir=None,
                                                        num_labels=len(label_list), 
                                                        id2label=id2label, 
                                                        label2id=label2id,
                                                        token=None,
                                                        )


    trainer_args = TrainingArguments(
                                optim="adamw_torch",
                                num_train_epochs=args.epochs,
                                output_dir = str("./output"),
                                evaluation_strategy="no",
                                save_strategy="no",
                                do_eval=False,
                                seed=args.seed,
                                full_determinism=True)
    
    tokenizer = AutoTokenizer.from_pretrained(args.model, 
                                              local_files_only=True, 
                                              padding=True, 
                                              num_labels=len(label_list))

    train_dataset_tokenized = dataset['train'].map(
                        utils.tokenize_and_align_labels,
                        batched=True,
                        desc="Running tokenizer on train dataset", 
                        fn_kwargs={"tokenizer": tokenizer, "b_to_i_label": b_to_i_label}
        ).remove_columns(['ner_tags', 'id', 'tokens'])

    data_collator = DataCollatorForTokenClassification(tokenizer)

    counterfactual_set_tokenized = counterfactual_set.map(
                    utils.tokenize_and_align_labels,
                    batched=True,
                    desc="Running tokenizer on validation dataset",
                    fn_kwargs={"tokenizer": tokenizer, "b_to_i_label": b_to_i_label}
                ).remove_columns(['ner_tags', 'id', 'tokens'])

    test_dataset_tokenized = dataset['test'].map(
                    utils.tokenize_and_align_labels,
                    batched=True,
                    desc="Running tokenizer on prediction dataset",
                    fn_kwargs={"toke-nizer": tokenizer, "b_to_i_label": b_to_i_label}
                ).remove_columns(['ner_tags', 'id', 'tokens'])

    trainer = Trainer(
            model=model.to(device),
            train_dataset=concatenate_datasets([train_dataset_tokenized, counterfactual_set_tokenized]).shuffle(args.seed),
            tokenizer=tokenizer,
            data_collator=data_collator,
            compute_metrics=utils.compute_metrics_wrapper(label_list, metric),
            args = trainer_args,
    )

    train_metrics = []
    test_metrics = []
    train_result = trainer.train()

    metrics = train_result.metrics
    train_metrics.append(train_result.metrics)

    max_train_samples = len(train_dataset_tokenized)
    metrics["train_samples"] = min(max_train_samples, len(train_dataset_tokenized))

    raw_predictions, labels, metricTest = trainer.predict(test_dataset_tokenized, metric_key_prefix="test")
    metricTest["AUGMENTATION_TIME"] = augmentation_time
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

    with pd.ExcelWriter(f"results/baselines/{dataset_name}/{xlsxoutput}") as writer:  
        train_df.to_excel(writer, sheet_name='train')
        test_df.to_excel(writer, sheet_name='test')
        print(f"Value saved in {xlsxoutput}")
