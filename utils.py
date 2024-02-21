import argparse
import numpy as np


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-model', default="dmis-lab/biobert-v1.1", type=str, help="Model name")
    parser.add_argument('-epochs', default=5, type=int, help='Number of training epochs')
    parser.add_argument('-seed', default=100, type=int, help="Seed for randomicity")
    parser.add_argument('-dataset', default='NCBI-disease-IOB', type=str, choices=["NCBI-disease-IOB", "BC5CDR-chem-IOB", "BC2GM-IOB"], help="\nNCBI-disease-IOB: diseases dataset,\nBC5CDR-chem-IOB: chemical dataset,\nBC2GM-IOB: genetic dataset")
    parser.add_argument('-length', default=108, type=int, help="Dataset length reduction")
    parser.add_argument('-reverse', default=0, type=int, choices=[0, 1], help='0: max\n 1: min')
    parser.add_argument('-budget', default=0, type=int, help="0: tutti gli esempi generati (local-gen); 100-300-500 global")
    parser.add_argument('-exr', default=10, type=int, help="numero di esempi generati per ciascuna entry con almeno una entità all'interno del dataset")
    args = parser.parse_args(argv)
    return args

def lexiconGeneration(dataset):
    #0: O, 1: B-***, 2:I-***
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

def update_v_concept(V_concept, V_context, C_concept):
    sim = max(0, np.dot(V_concept, V_context)/(np.linalg.norm(V_concept)*np.linalg.norm(V_context))) # Cosine similarity...
    lr = 1 / C_concept
    V_concept += lr * (1-sim) * V_context
    return V_concept