import os
import argparse
import numpy as np
from transformers_interpret import TokenClassificationExplainer

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-epochs', default=5, type=int, help='Number of training epochs')
    parser.add_argument('-seed', default=100, type=int, help="Seed for reproducibility")
    parser.add_argument('-dataset', default=r'data/ncbi.hf', type=str, choices=[r"data/ncbi.hf", r"data/bc5cdr.hf", r"data/bc2gm.hf"], help="\nNCBI-disease-IOB: diseases dataset,\nBC5CDR-chem-IOB: chemical dataset,\nBC2GM-IOB: genetic dataset")
    parser.add_argument('-length', default=108, type=int, help="Dataset length reduction")
    parser.add_argument('-reverse', default=0, type=int, choices=[0, 1], help='0: max\n 1: min')
    parser.add_argument('-budget', default=0, type=int, help="0: all the example generated (local-gen); 100-300-500 example (global-gen)")
    parser.add_argument('-exr', default=5, type=int, help="Number of example generated for each entry with at least one entity within the dataset")
    parser.add_argument('-xai', type=int, help="Sample to perform XAI on")
    parser.add_argument('-baseline', type=str, default=None, choices=['bert', 'biobert', 'lwtr', 'sr', 'mr'])
    args = parser.parse_args(argv)
    return args

def xai_model(model, tokenizer, training_sample):
    training_sample = ' '.join(training_sample['tokens'])
    ner_explainer = TokenClassificationExplainer(
        model,
        tokenizer,
    )

    ner_explainer(training_sample, ignored_labels=['O'])
    ner_explainer.visualize("bert_ner_viz.html")

def tokenize_and_align_labels(examples, tokenizer, b_to_i_label):
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
                    label_ids.append(label[word_idx])
                else:
                    label_ids.append(b_to_i_label[label[word_idx]])

                previous_word_idx = word_idx
            labels.append(label_ids)
        tokenized_inputs["labels"] = labels
        return tokenized_inputs

def compute_metrics_wrapper(label_list, metric):
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
    return compute_metrics

def clear_folder(folder):
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.remove(path)
            elif os.path.isdir(path):
                os.removedirs(path)
        except Exception as e:
            print(f"Error deleting {path}: {e}")