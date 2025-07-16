import os

class MELMAugmenter():
    def __init__(self, seed, train_data, valid_data):
        self.labels = {0: 'O', 1: 'B', 2: 'I'}
        self.inverse_label = {'O': 0, 'B': 1, 'I': 2}
        self.seed = seed
        os.chdir('MELM')
        with open("data/train.txt", "w") as f_out:
            for line in train_data:
                for txt, tag in zip(line["tokens"], line["ner_tags"]):
                    print("{}\t{}".format(txt, self.labels[tag]), file=f_out)
                print(file=f_out)

        with open("data/dev.txt", "w") as f_out:
            for line in valid_data:
                for txt, tag in zip(line["tokens"], line["ner_tags"]):
                    print("{}\t{}".format(txt, self.labels[tag]), file=f_out)
                print(file=f_out)
        os.chdir('..')

    def fit(self):
        os.chdir('MELM')
        os.system("01_train.sh")
        os.chdir('..')

    def augment_dataset(self):
        os.chdir('MELM')
        os.system("02_generate.sh {}".format(self.seed))
        final_json = []
        with open('data/aug.entity', 'r') as outfile:
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
        os.chdir('..')
        return final_json