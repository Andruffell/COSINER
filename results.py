import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import scipy.stats as st
class Result:
    def __init__(self, method:str, dataset:str, scenario:int, precision:tuple, recall:tuple, f1:tuple, time:tuple, budget=0, exr=0, reverse=0):
        self.result_dict = {
                       "method": method, 
                       "dataset": dataset, 
                       "scenario": scenario, 
                       "precision": precision, 
                       "recall": recall,
                       "f1": f1,
                       "time": time,
                       "budget": budget, 
                       "exr": exr, 
                       "max_min_similarity": "max" if reverse == 0 else "min"
                       }

def confidence_intervals(path, files, confidence=0.95):
    xlsx = [pd.ExcelFile(os.path.join(path, f'{x}')) for x in files]
    test = [pd.read_excel(xlsx[x], 1) for x in range(len(files))]

    df_test_concat = pd.concat(test)

    mean_recall = np.mean(df_test_concat['test_overall_recall'])
    recall = st.t.interval(confidence, len(df_test_concat['test_overall_recall'])-1, loc=mean_recall, scale=st.sem(df_test_concat['test_overall_recall']))
    recall_interval = recall[1]-mean_recall

    mean_precision = np.mean(df_test_concat['test_overall_precision'])
    precision = st.t.interval(confidence, len(df_test_concat['test_overall_precision'])-1, loc=mean_precision, scale=st.sem(df_test_concat['test_overall_precision']))
    precision_interval = precision[1]-mean_precision

    mean_f1 = np.mean(df_test_concat['test_overall_f1'])
    f1 = st.t.interval(confidence, len(df_test_concat['test_overall_f1'])-1, loc=mean_f1, scale=st.sem(df_test_concat['test_overall_f1']))
    f1_interval = f1[1]-mean_f1

    mean_augmentation_time = np.mean(df_test_concat['AUGMENTATION_TIME'])
    augmentation_time = st.t.interval(confidence, len(df_test_concat['AUGMENTATION_TIME'])-1, loc=mean_augmentation_time, scale=st.sem(df_test_concat['AUGMENTATION_TIME']))
    augmentation_time_interval = augmentation_time[1]-mean_augmentation_time

    return (round(mean_recall, 3), round(recall_interval, 3)), (round(mean_precision, 3), round(precision_interval, 3)), (round(mean_f1, 3), round(f1_interval, 3)), (round(mean_augmentation_time, 3), round(augmentation_time_interval, 3))

if __name__=="__main__":
    base_directory = os.getcwd()
    results_path = os.path.join(base_directory, "results")
    
    ### COSINER
    print("COSINER results")
    cosiner_results = []
    cosiner_path = os.path.join(results_path, "cosiner")
    os.chdir(cosiner_path)
    datasets = os.listdir()
    for dataset in datasets:
        dataset_path = os.path.join(cosiner_path, dataset)
        os.chdir(dataset_path)
        files = os.listdir()
        if ".gitignore" in files: files.remove(".gitignore")

        ### For baselines there is also baseline name
        dataset_name = list(set([x.split("_")[0] for x in files]))              # dataset name
        dataset_length = sorted(list(set([x.split("_")[1] for x in files])))    # few-shot scenario
        exr = [2, 5, 10]                                                        # new examples per sentence
        budget = [0, 100, 300, 500]                                             # local 0 - global 100, 300, 500
        reverse = [0, 1]                                                        # max similarity - min similarity

        for d in dataset_name:
            for l in dataset_length:
                for b in budget:
                    exr_values = exr if b == 0 else [10] # global augmentation works always with exr = 10
                    for e in exr_values:
                            for r in reverse:
                                file_name = f"{d}_{l}_{e}_{b}_{r}_"
                                found = [f for f in files if file_name in f]
                                scenario = 2 if l == min(dataset_length) else 10 if l == max(dataset_length) else 5
                                recall, precision, f1, augmentation_time = confidence_intervals(dataset_path, found)
                                x = Result("cosiner", d, scenario, list(precision), list(recall), list(f1), list(augmentation_time), b, e, r).result_dict
                                print(x)
                                cosiner_results.append(x)

    ### MELM
    print("MELM results")
    melm_results = []
    melm_path = os.path.join(results_path, "melm")
    os.chdir(melm_path)
    datasets = os.listdir()
    for dataset in datasets:
        dataset_path = os.path.join(melm_path, dataset)
        os.chdir(dataset_path)
        files = os.listdir()
        if ".gitignore" in files: files.remove(".gitignore")
        
        dataset_name = list(set([x.split("_")[0] for x in files]))              # dataset name
        dataset_length = sorted(list(set([x.split("_")[1] for x in files])))    # few-shot scenario

        for d in dataset_name:
            for l in dataset_length:
                file_name = f"{d}_{l}_"
                print(file_name)
                found = [f for f in files if file_name in f]
                scenario = 2 if l == min(dataset_length) else 10 if l == max(dataset_length) else 5
                recall, precision, f1, augmentation_time = confidence_intervals(dataset_path, found)
                print(f"Recall: {recall}")
                print(f"Precision: {precision}")
                print(f"F1: {f1}")
                print(f"Augmentation time: {augmentation_time} seconds")
                x = Result("melm", d, scenario, list(precision), list(recall), list(f1), list(augmentation_time), 0, 0, 0).result_dict
                print(x)
                melm_results.append(x)

    ### Style_NER
    print("Style_NER results")
    styleNER_results = []
    style_path = os.path.join(results_path, "style_NER")
    os.chdir(style_path)
    datasets = os.listdir()
    for dataset in datasets:
        dataset_path = os.path.join(style_path, dataset)
        os.chdir(dataset_path)
        files = os.listdir()
        if ".gitignore" in files: files.remove(".gitignore")
        
        dataset_name = list(set([x.split("_")[0] for x in files]))              # dataset name
        dataset_length = sorted(list(set([x.split("_")[1] for x in files])))    # few-shot scenario

        for d in dataset_name:
            for l in dataset_length:
                file_name = f"{d}_{l}_"
                print(file_name)
                found = [f for f in files if file_name in f]
                scenario = 2 if l == min(dataset_length) else 10 if l == max(dataset_length) else 5
                recall, precision, f1, augmentation_time = confidence_intervals(dataset_path, found)
                print(f"Recall: {recall}")
                print(f"Precision: {precision}")
                print(f"F1: {f1}")
                print(f"Augmentation time: {augmentation_time} seconds")
                x = Result("style_NER", d, scenario, list(precision), list(recall), list(f1), list(augmentation_time), 0, 0, 0).result_dict
                print(x)
                styleNER_results.append(x)

    ### LWTR; MR; SR
    print("Baselines results")
    baseline_results = []
    baseline_path = os.path.join(results_path, "baselines")
    os.chdir(baseline_path)
    datasets = os.listdir()
    for dataset in datasets:
        dataset_path = os.path.join(baseline_path, dataset)
        os.chdir(dataset_path)
        files = os.listdir()
        if ".gitignore" in files: files.remove(".gitignore")
        
        dataset_name = list(set([x.split("_")[0] for x in files]))              # dataset name
        baseline_name = ["lwtr", "mr", "sr"]
        dataset_length = sorted(list(set([x.split("_")[2] for x in files])))    # few-shot scenario

        for d in dataset_name:
            for bs in baseline_name:
                for l in dataset_length:
                    file_name = f"{d}_{bs}_{l}_"
                    print(file_name)
                    found = [f for f in files if file_name in f]
                    scenario = 2 if l == min(dataset_length) else 10 if l == max(dataset_length) else 5
                    recall, precision, f1, augmentation_time = confidence_intervals(dataset_path, found)
                    print(f"Recall: {recall}")
                    print(f"Precision: {precision}")
                    print(f"F1: {f1}")
                    print(f"Augmentation time: {augmentation_time} seconds")
                    x = Result(bs, d, scenario, list(precision), list(recall), list(f1), list(augmentation_time), 0, 0, 0).result_dict
                    print(x)
                    baseline_results.append(x)
    
    cosiner_results.extend(melm_results)
    cosiner_results.extend(styleNER_results)
    cosiner_results.extend(baseline_results)
    
    df = pd.DataFrame.from_records(cosiner_results)