import os
import json
import utils

class SNER_Augmenter():
    def __init__(self, seed, source_dataset, target_dataset, source_name, target_name):
        self.labels = {0: 'O', 1: 'B', 2: 'I'}
        self.inverse_label = {'O': 0, 'B': 1, 'I': 2}
        self.seed = seed
        self.source_name = source_name
        self.target_name = target_name

        os.chdir('style_NER')
        with open(f"data/ner/{source_name}/train.txt", "w") as f_out:
            for line in source_dataset['train']:
                for txt, tag in zip(line["tokens"], line["ner_tags"]):
                    print("{}\t{}".format(txt, self.labels[tag]), file=f_out)
                print(file=f_out)

        with open(f"data/ner/{source_name}/dev.txt", "w") as f_out:
            for line in target_dataset['train']:
                for txt, tag in zip(line["tokens"], line["ner_tags"]):
                    print("{}\t{}".format(txt, self.labels[tag]), file=f_out)
                print(file=f_out)

        with open(f"data/ner/{source_name}/test.txt", "w") as f_out:
            for line in target_dataset['test']:
                for txt, tag in zip(line["tokens"], line["ner_tags"]):
                    print("{}\t{}".format(txt, self.labels[tag]), file=f_out)
                print(file=f_out)
        os.chdir('..')

        os.system(f"python -m style_NER.src.commons.preproc_domain --input_dir ner/{source_name} --output_file linearized_domain/{source_name}")

    def fit(self):

        with open(f'style_NER/configs/exp_domain/{self.target_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        data['model']['lambda_coef']['lambda_cross'] = 0.0

        with open(f'style_NER/configs/exp_domain/{self.target_name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        # Run to learn the style
        os.system(f"python -m style_NER.src.exp_domain.main --config configs/exp_domain/{self.target_name}.json")

        with open(f'style_NER/configs/exp_domain/{self.target_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        data['model']['lambda_coef']['lambda_cross'] = 1.0

        with open(f'style_NER/configs/exp_domain/{self.target_name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        
        # Run for cross-domain
        os.system(f"echo 1 | python -m style_NER.src.exp_domain.main --config configs/exp_domain/{self.target_name}.json | echo 1")

    def augment_dataset(self):

        # Generation of augmented data
        os.system(f"echo 1 | python -m style_NER.src.exp_domain.main --config configs/exp_domain/{self.target_name}.json --mode generate --replicable")
        os.system(f"python -m style_NER.src.commons.postproc_domain --inp_file style_NER/checkpoints/{self.source_name}-{self.target_name}/predictions/src_train_src2tgt_greedy.txt --out_file style_NER/data/ner/{self.target_name}/aug1.conll")
        os.system(f"python -m style_NER.src.commons.postproc_domain --inp_file style_NER/checkpoints/{self.source_name}-{self.target_name}/predictions/src_train_src2tgt_top5.txt --out_file style_NER/data/ner/{self.target_name}/aug2.conll")

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