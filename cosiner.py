import copy
import numpy as np
import pandas as pd
from collections import Counter
from transformers import (
    AutoTokenizer,
    pipeline,
)
import datasets
from datasets import ClassLabel, Dataset

def update_v_concept(V_concept, V_context, C_concept):
    sim = max(0, np.dot(V_concept, V_context)/(np.linalg.norm(V_concept)*np.linalg.norm(V_context)))
    lr = 1 / C_concept
    V_concept += lr * (1-sim) * V_context
    return V_concept

def embedding_extraction(training_set, ontology):
    tokenizer = AutoTokenizer.from_pretrained("models/BioBERT/TOKENIZER", padding=True, local_files_only=True)
    pipe = pipeline('feature-extraction', model="models/BioBERT", tokenizer=tokenizer)
    embeddings = {}
    for entity, info in ontology.items():
        joinedEntity = ' '.join(entity)        
        c_concept = info[0]
        sentences = [sentence for sentence in info[1]]        
        object_set = []
        c = dict(Counter(sentences))
        for s in c.keys():
            object_set.append((training_set.filter(lambda example: int(example['id']) in [int(s)])[0], c[s]))            
        v_concept = 0
        for sentence in object_set:
            joinedSentence = ' '.join(sentence[0]['tokens'])
            tokenizedSentence = tokenizer(joinedSentence)['input_ids']
            tokenizedEntity = tokenizer(joinedEntity)['input_ids'][1:-1]

            for idx in range(sentence[1]):
                looking_index = 0
                start = 0
                end = 0
                for starting_index, token in enumerate(tokenizedSentence):
                    if token == tokenizedEntity[0]:
                        if looking_index == idx:
                            looking_list = tokenizedSentence[starting_index:starting_index+len(tokenizedEntity)]
                            if looking_list == tokenizedEntity:
                                start = starting_index
                                end = starting_index+len(tokenizedEntity)
                                looking_index += 1
                        else:
                            looking_index += 1

                words_embeddings = pipe(joinedSentence)
                v_context = np.array(words_embeddings[0])[start:end].mean(axis=0)

                if idx == 0:
                    v_concept = update_v_concept(v_context, v_context, c_concept)
                else:
                    v_concept = update_v_concept(v_concept, v_context, c_concept)       
        embeddings[' '.join(entity)] = v_concept

    return embeddings

def cosine_similarity(entityList, n, reverse=False):
    predictedSimilarity = {}
    for entity in entityList:
        predictedSimilarity[entity] = entityList[entity]
    
    similarityLists = {}
    for entity, embedding in predictedSimilarity.items():
        entitiesSimilarityList = {}
        for otherEntity, otherEmbedding in {k: predictedSimilarity[k] for k in set(list(predictedSimilarity.keys())) - set([entity])}.items():
            entitiesSimilarityList[otherEntity] = float(np.dot(embedding,otherEmbedding)/(np.linalg.norm(embedding)*np.linalg.norm(otherEmbedding)))

        entitiesSimilarityList = dict(sorted(entitiesSimilarityList.items(), key=lambda item: item[1], reverse=not reverse)[:n])
        similarityLists[entity] = entitiesSimilarityList

    return similarityLists

def augment_dataset(training_set, examples_per_row, similarityList, budget, reverse, label_list):
    counterfactualExamples = []
    appendingIndex = len(training_set)
    for row in training_set:
        if row['ner_tags'].count(1)>0:
            id = copy.deepcopy(row['id'])
            tokens = copy.deepcopy(row['tokens'])
            ner_tags = copy.deepcopy(row['ner_tags'])
            for j in range(examples_per_row):
                indexList = []
                newIndexList = []
                oldEntities = []
                for idx, (token, ner_tag) in enumerate(zip(tokens, ner_tags)):
                    if ner_tag == 1:
                        oldEntity = []
                        oldEntity.append(token)
                        newIndexList = []
                        newIndexList.append(tokens.index(token))
                        if len(tokens)-1 == idx:
                            oldEntities.append(oldEntity)
                            oldEntity = [] 
                            indexList.append(newIndexList)
                            newIndexList = []
                    elif ner_tag == 2:
                        oldEntity.append(token)
                        newIndexList.append(tokens.index(token))
                        if len(tokens)-1 == idx:
                            oldEntities.append(oldEntity)
                            oldEntity = [] 
                            indexList.append(newIndexList)
                            newIndexList = []
                    else:
                        if newIndexList != []:
                            indexList.append(newIndexList)
                            oldEntities.append(oldEntity)
                            oldEntity = []
                            newIndexList = []     
                similarityValue = []
                for idx, i in enumerate(range(len(indexList))):
                    entity = indexList[len(indexList)-1-i]
                    entityStart = entity[0]

                    for word in entity:
                        tokens.pop(entityStart)
                        ner_tags.pop(entityStart)

                    oldEntity = " ".join(oldEntities[idx])
                    newDisease = [list(similarityList[oldEntity])[j]]
                    similarityValue.append(list(similarityList[oldEntity].values())[j])
                    for idx, word in enumerate(newDisease):
                        tokens.insert(entityStart+idx, word)
                        if idx == 0:
                            ner_tags.insert(entityStart+idx, 1)
                        else:
                            ner_tags.insert(entityStart+idx, 2)

                newExample = copy.deepcopy([str(appendingIndex), tokens, ner_tags])
                finalValue = np.mean(similarityValue)
                counterfactualExamples.append((newExample, finalValue))
                appendingIndex += 1
                id = copy.deepcopy(row['id'])
                tokens = copy.deepcopy(row['tokens'])
                ner_tags = copy.deepcopy(row['ner_tags'])

    budget = len(counterfactualExamples) if budget == 0 or budget > len(counterfactualExamples) else budget
    counterfactualExamples = sorted(counterfactualExamples, key=lambda item: item[1], reverse=not reverse)[0: budget]
    counterfactualExamples = list(zip(*counterfactualExamples))[0]
    counterfactual_set = Dataset.from_pandas(pd.DataFrame(counterfactualExamples, columns=["id", "tokens", "ner_tags"]))
    counterfactual_set.features["ner_tags"] = datasets.features.Sequence(ClassLabel(names=label_list))
    return counterfactual_set