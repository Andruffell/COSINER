import os
import sys
import subprocess
import json
import utils
from datasets import Dataset

def convert_chemdner(dataset):
    train_tokens = []
    train_ner_tags = []
    test_tokens = []
    test_ner_tags = []

    for line in dataset["train"]:
        matched_words = line["entities"]
        sentence = line["text"].split()
        labels = [0] * len(sentence)

        for entity in matched_words:
            words = entity.split()
            if len(words) == 1:
                for word in sentence:
                    if entity in word:
                        labels[sentence.index(word)] = 1
            else:
                i=0
                for entity in words:
                    try:
                        for word in sentence:
                            if entity in word:
                                if i == 0:
                                    labels[sentence.index(word)] = 1
                                else:
                                    labels[sentence.index(word)] = 2
                                i+=1
                    except:
                        pass
        if len(sentence) == len(labels):
            if line["split"] == "train":
                train_tokens.append(sentence)
                train_ner_tags.append(labels)
            else:
                test_tokens.append(sentence)
                test_ner_tags.append(labels)
        else:
            print(len(sentence))
            print(len(labels))
            print("Error")


    train_dataset = Dataset.from_dict({"tokens": train_tokens, "ner_tags": train_ner_tags})
    test_dataset = Dataset.from_dict({"tokens": test_tokens, "ner_tags": test_ner_tags})

    return train_dataset, test_dataset

class SNER_Augmenter():
    def __init__(self, seed, source_dataset, target_dataset, source_name, target_name):
        self.labels = {0: 'O', 1: 'B', 2: 'I'}
        self.inverse_label = {'O': 0, 'B': 1, 'I': 2}
        self.seed = seed
        self.source_name = source_name
        self.target_name = target_name
        
        if source_name == "chemdner":
            source_dataset['train'], source_dataset['test'] = convert_chemdner(source_dataset)

        os.chdir('style_NER')
        with open(f"data/ner/{source_name}/train.txt", "w", encoding="utf-8") as f_out:
            for line in source_dataset['train']:
                for txt, tag in zip(line["tokens"], line["ner_tags"]):
                    if tag % 2 == 0 and tag != 0: tag = 2 
                    elif tag % 2 == 1 and tag != 0: tag = 1
                    print("{}\t{}".format(txt, self.labels[tag]), file=f_out)
                print(file=f_out)

        with open(f"data/ner/{source_name}/dev.txt", "w", encoding="utf-8") as f_out:
            for line in source_dataset['train']:
                for txt, tag in zip(line["tokens"], line["ner_tags"]):
                    if tag % 2 == 0 and tag != 0: tag = 2 
                    elif tag % 2 == 1 and tag != 0: tag = 1
                    print("{}\t{}".format(txt, self.labels[tag]), file=f_out)
                print(file=f_out)

        with open(f"data/ner/{source_name}/test.txt", "w", encoding="utf-8") as f_out:
            for line in source_dataset['test']:
                for txt, tag in zip(line["tokens"], line["ner_tags"]):
                    if tag % 2 == 0 and tag != 0: tag = 2 
                    elif tag % 2 == 1 and tag != 0: tag = 1
                    print("{}\t{}".format(txt, self.labels[tag]), file=f_out)
                print(file=f_out)

        with open(f"data/ner/{target_name}/train.txt", "w") as f_out:
            for line in target_dataset['train']:
                for txt, tag in zip(line["tokens"], line["ner_tags"]):
                    if tag % 2 == 0 and tag != 0: tag = 2 
                    elif tag % 2 == 1 and tag != 0: tag = 1
                    print("{}\t{}".format(txt, self.labels[tag]), file=f_out)
                print(file=f_out)

        with open(f"data/ner/{target_name}/dev.txt", "w") as f_out:
            for line in target_dataset['train']:
                for txt, tag in zip(line["tokens"], line["ner_tags"]):
                    if tag % 2 == 0 and tag != 0: tag = 2 
                    elif tag % 2 == 1 and tag != 0: tag = 1
                    print("{}\t{}".format(txt, self.labels[tag]), file=f_out)
                print(file=f_out)

        with open(f"data/ner/{target_name}/test.txt", "w") as f_out:
            for line in target_dataset['test']:
                for txt, tag in zip(line["tokens"], line["ner_tags"]):
                    if tag % 2 == 0 and tag != 0: tag = 2 
                    elif tag % 2 == 1 and tag != 0: tag = 1
                    print("{}\t{}".format(txt, self.labels[tag]), file=f_out)
                print(file=f_out)
        os.chdir('..')

        subprocess.run([sys.executable, "-m", "style_NER.src.commons.preproc_domain", "--input_dir", f"ner/{source_name}", "--output_file", f"linearized_domain/{source_name}"])
        subprocess.run([sys.executable, "-m", "style_NER.src.commons.preproc_domain", "--input_dir", f"ner/{target_name}", "--output_file", f"linearized_domain/{target_name}"])

    def fit(self):

        with open(f'style_NER/configs/exp_domain/{self.target_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        data['model']['lambda_coef']['lambda_cross'] = 0.0

        with open(f'style_NER/configs/exp_domain/{self.target_name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        # Run to learn the style
        subprocess.run([sys.executable, "-m", "style_NER.src.exp_domain.main", "--config", f"configs/exp_domain/{self.target_name}.json"])

        with open(f'style_NER/configs/exp_domain/{self.target_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        data['model']['lambda_coef']['lambda_cross'] = 1.0

        with open(f'style_NER/configs/exp_domain/{self.target_name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        
        # Run for cross-domain
        subprocess.run([sys.executable, "-m", "style_NER.src.exp_domain.main", "--config", f"configs/exp_domain/{self.target_name}.json"],input="1\n", text=True)

    def augment_dataset(self):
        # Generation of augmented data
        subprocess.run([sys.executable, "-m", "style_NER.src.exp_domain.main", "--config", f"configs/exp_domain/{self.target_name}.json", "--mode", "generate", "--replicable"], input="1\n", text=True)
        subprocess.run([sys.executable, "-m", "style_NER.src.commons.postproc_domain", "--inp_file", f"style_NER/checkpoints/{self.source_name}-{self.target_name}/predictions/src_train_src2tgt_greedy.txt", "--out_file", f"style_NER/data/ner/{self.target_name}/aug1.conll"])        
        subprocess.run([sys.executable, "-m", "style_NER.src.commons.postproc_domain", "--inp_file", f"style_NER/checkpoints/{self.source_name}-{self.target_name}/predictions/src_train_src2tgt_top5.txt", "--out_file", f"style_NER/data/ner/{self.target_name}/aug2.conll"])
        final_json = []
        with open(f'style_NER/data/ner/{self.target_name}/aug1.conll', 'r') as outfile:
            tokens = []
            ner_tags = []
            for lines in outfile:
                if lines == '\n':
                    if tokens != []:
                        final_json.append({"id": None, "tokens": tokens, "ner_tags": ner_tags})
                    tokens = []
                    ner_tags = []
                else:
                    if len(lines.split()) <= 1:
                        tok = ' '
                        tag = 'O'
                    else:
                        tok = lines.split()[0]
                        tag = lines.split()[1]
                    tokens.append(tok)
                    ner_tags.append(self.inverse_label[tag])


        with open(f'style_NER/data/ner/{self.target_name}/aug2.conll', 'r') as outfile:
            tokens = []
            ner_tags = []
            for lines in outfile:
                if lines == '\n':
                    if tokens != []:
                        final_json.append({"id": None, "tokens": tokens, "ner_tags": ner_tags})
                    tokens = []
                    ner_tags = []
                else:
                    if len(lines.split()) <= 1:
                        tok = ' '
                        tag = 'O'
                    else:
                        tok = lines.split()[0]
                        tag = lines.split()[1]
                    tokens.append(tok)
                    ner_tags.append(self.inverse_label[tag])
        
        utils.clear_folder(f"style_NER/checkpoints/{self.source_name}-{self.target_name}")        
        os.remove(f'style_NER/data/ner/{self.target_name}/aug1.conll')                   
        os.remove(f'style_NER/data/ner/{self.target_name}/aug2.conll')
        return final_json