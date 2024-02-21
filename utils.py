import argparse
import re
import numpy as np
import torch

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-model', default="dmis-lab/biobert-v1.1", type=str, help="Model name")
    parser.add_argument('-epochs', default=5, type=int, help='Number of training epochs')
    parser.add_argument('-seed', default=100, type=int, help="Seed for randomicity")
    parser.add_argument('-dataset', default='NCBI-disease-IOB', type=str, choices=["NCBI-disease-IOB", "BC5CDR-chem-IOB", "BC2GM-IOB"], help="#NCBI-disease-IOB: diseases dataset, BC5CDR-chem-IOB: chemical dataset, BC2GM-IOB: genetic dataset")
    parser.add_argument('-length', default=108, type=int, help="Dataset length reduction")
    parser.add_argument('-reverse', default=0, type=int, choices=[0, 1], help='0: descending, 1:ascending')
    parser.add_argument('-budget', default=0, type=int, help="0: tutti gli esempi generati (local-gen); 100-300-500 global")
    parser.add_argument('-exr', default=10, type=int, help="numero di esempi generati per ciascuna entry con almeno una entità all'interno del dataset")
    args = parser.parse_args(argv)
    return args

def ontologyGeneration(dataset):
    #0: O, 1: B-***, 2:I-***
    ontology = {}

    for row in dataset:
        id = row['id']
        tokens = row['tokens']
        ner_tags = row['ner_tags']
        newDisease = []
        tokens_len = len(tokens)-1
        for idx, (token, ner_tag) in enumerate(zip(tokens, ner_tags)):
            if ner_tag == 1: #"B-***"
                if newDisease != []:
                    if tuple(newDisease) in ontology:
                        ontology[tuple(newDisease)][0] += 1
                        ontology[tuple(newDisease)][1].append(id)
                    else:
                        ontology[tuple(newDisease)] = [1, [id]]
                    newDisease = []
                newDisease.append(token)      
                if tokens_len == idx:
                    if tuple(newDisease) in ontology:
                        ontology[tuple(newDisease)][0] += 1
                        ontology[tuple(newDisease)][1].append(id)
                    else:
                        ontology[tuple(newDisease)] = [1, [id]]
                    newDisease = []
            elif ner_tag == 2: #"I-***"
                newDisease.append(token)
                if tokens_len == idx:
                    if tuple(newDisease) in ontology:
                        ontology[tuple(newDisease)][0] += 1
                        ontology[tuple(newDisease)][1].append(id)
                    else:
                        ontology[tuple(newDisease)] = [1, [id]]
                    newDisease = []
            else:
                if (newDisease != []):
                    if tuple(newDisease) in ontology:
                        ontology[tuple(newDisease)][0] += 1
                        ontology[tuple(newDisease)][1].append(id)
                    else:
                        ontology[tuple(newDisease)] = [1, [id]]
                    newDisease = []

    ontology = dict(sorted(ontology.items(), key=lambda item: item[1], reverse=True))
    print("L'ontologia estratta dal dataset contiene {} entità".format(len(ontology)))
    return ontology


# def copertura(trainOnt, validOnt):
#     malattieOntList = [" ".join(malattia) for malattia in trainOnt]
#     validOntList = [" ".join(malattia) for malattia in validOnt]
#     validOntListReg = [re.sub('\W+', '', i.lower()) for i in validOntList]
#     nuoveMalattieReg = [re.sub('\W+', '', i.lower()) for i in malattieOntList]

#     nuoveCoperte = 0
#     indices = []

#     for malattia in nuoveMalattieReg:
#         if malattia in validOntListReg:
#             nuoveCoperte += 1
#             newIndex = validOntListReg.index(malattia)
#             print(newIndex, malattia)
#             indices.append(newIndex)
            
#     returnList = []
#     for index in indices:
#         returnList.append(validOntList[index])
#     print("Lunghezza finale lista:", len(returnList))    
#     return returnList

# def extract_small_set(ontology, dataset):
#     entityList = [" ".join(entity) for entity in ontology]
#     entityListReg = [i.lower() for i in entityList]
#     indexList = set()
#     entitySet = set()
#     for row in dataset:
#         id = row['id']
#         frase = " ".join(row['tokens'])
#         for malattia in entityListReg:
#             if malattia in frase.lower():
#                 indexList.add(id)
#                 entitySet.add(entityList[entityListReg.index(malattia)])
                
#     small_dataset = dataset.filter(lambda example: example['id'] in list(indexList))
#     return small_dataset

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

# def tokenize_and_align_labels(examples):
#         tokenized_inputs = tokenizer(
#             examples['tokens'],
#             padding="max_length",
#             truncation=True,
#             max_length=512,
#             is_split_into_words=True,
#         )
#         labels = []
#         for i, label in enumerate(examples["ner_tags"]):
#             word_ids = tokenized_inputs.word_ids(batch_index=i)
#             previous_word_idx = None
#             label_ids = []
#             for word_idx in word_ids:
#                 # Special tokens have a word id that is None. We set the label to -100 so they are automatically
#                 # ignored in the loss function.
#                 if word_idx is None:
#                     label_ids.append(-100)
#                 # We set the label for the first token of each word.
#                 elif word_idx != previous_word_idx:
#                     label_ids.append(label_to_id[label[word_idx]])
#                 # For the other tokens in a word, we set the label to either the current label or -100, depending on
#                 # the label_all_tokens flag.
#                 else:
#                     label_ids.append(b_to_i_label[label_to_id[label[word_idx]]])

#                 previous_word_idx = word_idx

#             labels.append(label_ids)
#         tokenized_inputs["labels"] = labels
#         return tokenized_inputs

# def compute_metrics(p):
#         predictions, labels = p
#         predictions = np.argmax(predictions, axis=2)

#         # Remove ignored index (special tokens)
#         true_predictions = [
#             [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
#             for prediction, label in zip(predictions, labels)
#         ]
#         true_labels = [
#             [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
#             for prediction, label in zip(predictions, labels)
#         ]
#         metric = load_metric("seqeval")
#         results = metric.compute(predictions=true_predictions, references=true_labels)
#         if True:
#             # Unpack nested dictionaries
#             final_results = {}
#             for key, value in results.items():
#                 if isinstance(value, dict):
#                     for n, v in value.items():
#                         final_results[f"{key}_{n}"] = v
#                 else:
#                     final_results[key] = value
#             return final_results
#         else:
#             return {
#                 "precision": results["overall_precision"],
#                 "recall": results["overall_recall"],
#                 "f1": results["overall_f1"],
#                 "accuracy": results["overall_accuracy"],
#             }
        
        
def get_label_list(labels):
        unique_labels = set()
        for label in labels:
            unique_labels = unique_labels | set(label)
        label_list = list(unique_labels)
        label_list.sort()
        return label_list

def update_v_concept(V_concept, V_context, C_concept):
    sim = max(0, np.dot(V_concept, V_context)/(np.linalg.norm(V_concept)*np.linalg.norm(V_context))) # Cosine similarity...
    lr = 1 / C_concept
    V_concept += lr * (1-sim) * V_context
    return V_concept