import sys

import pandas as pd
import torch
import evaluate
import random

from datasets import load_from_disk
from transformers import (AutoModelForTokenClassification, 
                          Trainer, 
                          AutoTokenizer, 
                          DataCollatorForTokenClassification, 
                          TrainingArguments, 
                          set_seed,
                          enable_full_determinism)

from lexicon_generator import LexiconGenerator
import cosiner
import utils

if __name__ == '__main__':
    args = utils.parse_args(sys.argv[1:])
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(device)

    print(args)
    set_seed(args.seed)
    enable_full_determinism(args.seed)
    dataset_name = args.dataset.split('/')[-1].split('.')[0]

    xlsxoutput = f"{dataset_name}_{str(args.length)}_{str(args.exr)}_{str(args.budget)}_{str(args.reverse)}_{str(args.seed)}.xlsx"
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

    samples_num = random.sample(range(len(dataset['train'])), args.length)
    dataset['train'] = dataset['train'].select(samples_num) if args.length > 0 else dataset['train']
    print(dataset['train'])

    lexicon = LexiconGenerator("cosiner").lexicon_generation_method(dataset['train']) #Lexicon generation using entities
    embeddings = cosiner.embedding_extraction(args.model, dataset['train'], lexicon)
    similarityList = cosiner.cosine_similarity(embeddings, args.exr, args.reverse)

    eligible_rows = 0
    for row_check in dataset['train']:
        if row_check['ner_tags'].count(1)>0:
            eligible_rows +=1
    print("Eligible rows: {}".format(eligible_rows))

    counterfactual_set = cosiner.augment_dataset(dataset['train'], args.exr, similarityList, args.budget, args.reverse, label_list)

    model = AutoModelForTokenClassification.from_pretrained(
                                                        args.model,
                                                        cache_dir=None,
                                                        num_labels=len(label_list), 
                                                        id2label=id2label, 
                                                        label2id=label2id,
                                                        token=None,
                                                        )
    
    tokenizer = AutoTokenizer.from_pretrained(args.model, 
                                              local_files_only=True, 
                                              padding=True, 
                                              num_labels=len(label_list))

    trainer_args = TrainingArguments(
                                optim="adamw_torch",
                                num_train_epochs=args.epochs,
                                output_dir = str("./output"),
                                evaluation_strategy="no",
                                save_strategy="no",
                                do_eval=False,
                                seed=args.seed,
                                full_determinism=True)
    
    data_collator = DataCollatorForTokenClassification(tokenizer)

    train_dataset = dataset['train'].map(
                        utils.tokenize_and_align_labels,
                        batched=True,
                        desc="Running tokenizer on train dataset", 
                        fn_kwargs={"tokenizer": tokenizer, "b_to_i_label": b_to_i_label}
        ).remove_columns(['ner_tags', 'id', 'tokens'])
    
    counterfactual_set_tokenized = counterfactual_set.map(
                    utils.tokenize_and_align_labels,
                    batched=True,
                    desc="Running tokenizer on validation dataset",
                    fn_kwargs={"tokenizer": tokenizer, "b_to_i_label": b_to_i_label}
                ).remove_columns(['ner_tags', 'id', 'tokens'])

    predict_dataset = dataset['test'].map(
                    utils.tokenize_and_align_labels,
                    batched=True,
                    desc="Running tokenizer on prediction dataset",
                    fn_kwargs={"tokenizer": tokenizer, "b_to_i_label": b_to_i_label}
                ).remove_columns(['ner_tags', 'id', 'tokens'])
    
    trainer = Trainer(
            model=model.to("cuda:0"),
            train_dataset=train_dataset,
            tokenizer=tokenizer,
            data_collator=data_collator,
            compute_metrics=utils.compute_metrics_wrapper(label_list, metric),
            args = trainer_args,
    )

    train_metrics = []
    test_metrics = []
    train_result = trainer.train()
    print(train_result)
    metrics = train_result.metrics
    train_metrics.append(train_result.metrics)

    max_train_samples = len(train_dataset)
    metrics["train_samples"] = min(max_train_samples, len(train_dataset))

    raw_predictions, labels, metricTest = trainer.predict(predict_dataset, metric_key_prefix="test")
    test_metrics.append(metricTest)
    print(test_metrics)

    if args.xai:
        utils.xai_model(model, tokenizer, dataset['train'][args.xai])

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

    with pd.ExcelWriter(f"results/cosiner/{dataset_name}/{xlsxoutput}") as writer:  
        train_df.to_excel(writer, sheet_name='train')
        test_df.to_excel(writer, sheet_name='test')
