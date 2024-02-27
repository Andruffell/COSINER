import numpy as np
import pandas as pd
import copy 
import random
import datasets
from datasets import ClassLabel, Dataset
from nltk.corpus import wordnet as wn

def syn_with_word_net(dataset, label_list):
    counterfactualExamples = []
    appendingIndex = len(dataset)
              
    for row in dataset:
        tokens = row['tokens']
        ner_tags = row['ner_tags']
        indexList = []
        newIndexList = []
        
        x = list(np.random.binomial(1, 0.5, len(tokens)))
        for idx, (token, ner_tag) in enumerate(zip(tokens, ner_tags)):
            if x[idx] == 1:
                if wn.synsets(token) != []:
                    syn = wn.synsets(token)[0]
                    if len(syn.lemmas()) > 1:
                        tokens[idx] = syn.lemmas()[1].name()

        newExample = copy.deepcopy([str(appendingIndex), tokens, ner_tags])
        counterfactualExamples.append(newExample)
        appendingIndex += 1

    counterfactual_set = Dataset.from_pandas(pd.DataFrame(counterfactualExamples, columns=["id", "tokens", "ner_tags"]))
    new_features = counterfactual_set.features.copy()
    new_features["ner_tags"] = datasets.features.features.Sequence(ClassLabel(names=label_list))
    counterfactual_set = counterfactual_set.cast(new_features)
    return counterfactual_set


def single_word_generation(dataset, label):
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

def lwt_replacement(dataset, label_list):
    counterfactualExamples = []
    appendingIndex = len(dataset)
    o_ontology = single_word_generation(dataset, 0)
    b_ontology = single_word_generation(dataset, 1)
    i_ontology = single_word_generation(dataset, 2)
              
    for row in dataset:
        id = appendingIndex
        tokens = row['tokens']
        ner_tags = row['ner_tags']
        indexList = []
        newIndexList = []
        
        x = list(np.random.binomial(1, 0.5, len(tokens)))
        for idx, (token, ner_tag) in enumerate(zip(tokens, ner_tags)):
            if x[idx] == 1:
                if ner_tag == 0:
                    tokens[idx] = random.sample(o_ontology, 1)[0]
                elif ner_tag == 1:
                    tokens[idx] = random.sample(b_ontology, 1)[0]
                else:
                    tokens[idx] = random.sample(i_ontology, 1)[0]

        newExample = copy.deepcopy([id, tokens, ner_tags])
        counterfactualExamples.append(newExample)
        appendingIndex += 1

    counterfactual_set = Dataset.from_pandas(pd.DataFrame(counterfactualExamples, columns=["id", "tokens", "ner_tags"]))
    new_features = counterfactual_set.features.copy()
    new_features["ner_tags"] = datasets.features.features.Sequence(ClassLabel(names=label_list))
    counterfactual_set = counterfactual_set.cast(new_features)
    return counterfactual_set

def lexiconGeneration(dataset, label_list):
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

def mention_replacement(dataset, ontology, label_list):
    counterfactualExamples = []
    appendingIndex = len(dataset)

    eligible_rows = 0
    for row_check in dataset:
        if row_check['ner_tags'].count(0)!=len(row_check['ner_tags']):
            eligible_rows +=1
          
    for row in dataset:
        if row['ner_tags'].count(0)<len(row['ner_tags']):
            id = appendingIndex
            tokens = row['tokens']
            ner_tags = row['ner_tags']

            indexList = []
            newIndexList = []
            oldEntities = []
            oldEntity = []
            ontology_index = int((ner_tags[0]-1)/2) 
            tokens_len = len(tokens)-1
            for idx, (token, ner_tag) in enumerate(zip(tokens, ner_tags)):
                if ner_tag % 2 == 1:
                    if oldEntity == []:
                        oldEntity.append(token)
                        newIndexList.append(idx)
                        if tokens_len == idx:
                            ontology_index = int((ner_tag-1)/2)
                            oldEntities.append((oldEntity, ontology_index))
                            oldEntity = [] 
                            indexList.append(newIndexList)
                            newIndexList = []
                    else:
                        oldEntities.append((oldEntity, ontology_index))
                        oldEntity = [] 
                        oldEntity.append(token)
                        indexList.append(newIndexList)
                        newIndexList = []
                        newIndexList.append(idx)
                elif ner_tag % 2 == 0 and ner_tag != 0:
                    oldEntity.append(token)
                    newIndexList.append(idx)
                    if tokens_len == idx:
                        oldEntities.append((oldEntity, ontology_index))
                        oldEntity = [] 
                        indexList.append(newIndexList)
                        newIndexList = []
                else:
                    if newIndexList != []:
                        oldEntities.append((oldEntity, ontology_index))
                        oldEntity = []
                        indexList.append(newIndexList)
                        newIndexList = []
                ontology_index = int((ner_tag-1)/2)

            x = list(np.random.binomial(1, 0.5, len(indexList)))
            if x.count(1) > 0:
                for idx, i in enumerate(range(len(indexList))):
                    if x[idx] == 1:
                        disease = indexList[len(indexList)-1-i]
                        diseaseStart = disease[0]

                        for word in disease:
                            tokens.pop(diseaseStart)
                            ner_tags.pop(diseaseStart)

                        newDisease = oldEntities[idx][0]

                        while newDisease == oldEntities[idx][0]:
                            randomTuple = random.sample(ontology[oldEntities[idx][1]],1)
                            newDisease = [list(i) for i in randomTuple][0]

                        for idx, word in enumerate(newDisease):
                            tokens.insert(diseaseStart+idx, word)
                            if idx == 0:
                                ner_tags.insert(diseaseStart+idx, 1)
                            else:
                                ner_tags.insert(diseaseStart+idx, 2)

                newExample = copy.deepcopy([id, tokens, ner_tags])
                counterfactualExamples.append(newExample)
                appendingIndex += 1

    counterfactual_set = Dataset.from_pandas(pd.DataFrame(counterfactualExamples, columns=["id", "tokens", "ner_tags"]))
    new_features = counterfactual_set.features.copy()
    new_features["ner_tags"] = datasets.features.features.Sequence(ClassLabel(names=label_list))
    counterfactual_set = counterfactual_set.cast(new_features)
    return counterfactual_set