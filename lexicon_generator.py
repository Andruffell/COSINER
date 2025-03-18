class LexiconGenerator():
    def __init__(self, lexicon_generation_method:str):
        self.lexicon_generation_method = lexicon_generation_method

    def cosinerLexiconGeneration(dataset):
        lexicon = {}

        for row in dataset:
            id = row['id']
            tokens = row['tokens']
            ner_tags = row['ner_tags']
            newEntity = []
            tokens_len = len(tokens)-1
            for idx, (token, ner_tag) in enumerate(zip(tokens, ner_tags)):
                if ner_tag == 1: #"B-***"
                    if newEntity != []:
                        if tuple(newEntity) in lexicon:
                            lexicon[tuple(newEntity)][0] += 1
                            lexicon[tuple(newEntity)][1].append(id)
                        else:
                            lexicon[tuple(newEntity)] = [1, [id]]
                        newEntity = []
                    newEntity.append(token)      
                    if tokens_len == idx:
                        if tuple(newEntity) in lexicon:
                            lexicon[tuple(newEntity)][0] += 1
                            lexicon[tuple(newEntity)][1].append(id)
                        else:
                            lexicon[tuple(newEntity)] = [1, [id]]
                        newEntity = []
                elif ner_tag == 2: #"I-***"
                    newEntity.append(token)
                    if tokens_len == idx:
                        if tuple(newEntity) in lexicon:
                            lexicon[tuple(newEntity)][0] += 1
                            lexicon[tuple(newEntity)][1].append(id)
                        else:
                            lexicon[tuple(newEntity)] = [1, [id]]
                        newEntity = []
                else:
                    if (newEntity != []):
                        if tuple(newEntity) in lexicon:
                            lexicon[tuple(newEntity)][0] += 1
                            lexicon[tuple(newEntity)][1].append(id)
                        else:
                            lexicon[tuple(newEntity)] = [1, [id]]
                        newEntity = []

        lexicon = dict(sorted(lexicon.items(), key=lambda item: item[1], reverse=True))
        print("The extracted lexicon contains {} entities".format(len(lexicon)))
        return lexicon
    
    def baselineLexiconGeneration(dataset, label_list):
        entities_num = int((len(label_list)-1)/2)
        lexicons = []
        for x in range(entities_num):
            lexicons.append(set())
        # 0: O, dispari: B, pari: I
        #Complessità O(m * n) dove m è la lunghezza media di ciascuna frase. Nel caso dei dataset completi n >> m. In contesto few shot n ~ m
        for row in dataset:
            tokens = row['tokens']
            ner_tags = row['ner_tags']
            newEntity = []
            tokens_len = len(tokens)-1
            if ner_tags != []:
                lexicon_index = int((ner_tags[0]-1)/2)
                for idx, (token, ner_tag) in enumerate(zip(tokens, ner_tags)):
                    if ner_tag % 2 == 1: #"B-***":
                        if newEntity != []:
                            lexicons[lexicon_index].add(tuple(newEntity)) # caso ...B B... (prima B)
                            newEntity = []
                        newEntity.append(token) # caso ...B B I... (seconda B)
                        if tokens_len == idx:
                            lexicon_index = int((ner_tag-1)/2)
                            lexicons[lexicon_index].add(tuple(newEntity)) #caso ... B]
                            newEntity = []
                    elif ner_tag % 2 == 0 and ner_tag != 0: #"I-***"
                        newEntity.append(token)
                        if tokens_len == idx:
                            lexicons[lexicon_index].add(tuple(newEntity)) #caso B I ... I]
                            newEntity = []
                    else:
                        if newEntity != []:
                            lexicons[lexicon_index].add(tuple(newEntity)) #caso B I ...I 0
                            newEntity = []
                    lexicon_index = int((ner_tag-1)/2)

        return lexicons
    
    def singleWordLexiconGeneration(dataset, label):
        #0: O, 1: B-***, 2:I-***
        lexicon = set()

        for row in dataset:
            #id = row['id']
            tokens = row['tokens']
            ner_tags = row['ner_tags']
            tokens_len = len(tokens)-1
            for idx, (token, ner_tag) in enumerate(zip(tokens, ner_tags)):
                if ner_tag == label:
                    if len(token) > 1:
                        lexicon.add(token)

        lexicon = list(lexicon)
        return lexicon