import argparse
import numpy as np
from transformers import AutoModelForTokenClassification, AutoTokenizer
from transformers_interpret import TokenClassificationExplainer

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-model', default="dmis-lab/biobert-v1.1", type=str, help="Model name")
    parser.add_argument('-epochs', default=5, type=int, help='Number of training epochs')
    parser.add_argument('-seed', default=100, type=int, help="Seed for randomicity")
    parser.add_argument('-dataset', default='NCBI-disease-IOB', type=str, choices=["NCBI-disease-IOB", "BC5CDR-chem-IOB", "BC2GM-IOB"], help="\nNCBI-disease-IOB: diseases dataset,\nBC5CDR-chem-IOB: chemical dataset,\nBC2GM-IOB: genetic dataset")
    parser.add_argument('-length', default=108, type=int, help="Dataset length reduction")
    parser.add_argument('-reverse', default=0, type=int, choices=[0, 1], help='0: max\n 1: min')
    parser.add_argument('-budget', default=0, type=int, help="0: tutti gli esempi generati (local-gen); 100-300-500 global")
    parser.add_argument('-exr', default=5, type=int, help="numero di esempi generati per ciascuna entry con almeno una entità all'interno del dataset")
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