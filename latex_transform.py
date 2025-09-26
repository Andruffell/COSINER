import pandas as pd
from scipy.stats import pearsonr, spearmanr

def convert_to_latex_t1(df):
    
    ncbi_max_global_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 2)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 2% - global - max similarity

    ncbi_max_global_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 5)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 5% - global - max similarity
    
    ncbi_max_global_10 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 10)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 10% - global - max similarity
    
    ncbi_min_global_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 2)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 2% - global - max similarity

    ncbi_min_global_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 5)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 5% - global - max similarity
    
    ncbi_min_global_10 = df[
            (df['method'] == "cosiner")
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 10)
          & (df["budget"] != 0)
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 10% - global - max similarity
    
    ncbi_max_local_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 2)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 2% - local - max similarity

    ncbi_max_local_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 5)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 5% - local - max similarity
    
    ncbi_max_local_10 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 10)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 10% - local - max similarity
    
    ncbi_min_local_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 2)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 2% - local - max similarity

    ncbi_min_local_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 5)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 5% - local - max similarity
    
    ncbi_min_local_10 = df[
            (df['method'] == "cosiner")
          & (df['dataset'] == 'ncbi')
          & (df['scenario'] == 10)
          & (df["budget"] == 0)
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # NCBI - 10% - local - max similarity
    
    bc5cdr_max_global_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 2)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 2% - global - max similarity

    bc5cdr_max_global_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 5)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 5% - global - max similarity
    
    bc5cdr_max_global_10 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 10)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 10% - global - max similarity
    
    bc5cdr_min_global_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 2)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 2% - global - max similarity

    bc5cdr_min_global_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 5)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 5% - global - max similarity
    
    bc5cdr_min_global_10 = df[
            (df['method'] == "cosiner")
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 10)
          & (df["budget"] != 0)
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 10% - global - max similarity
    
    bc5cdr_max_local_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 2)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 2% - local - max similarity

    bc5cdr_max_local_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 5)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 5% - local - max similarity
    
    bc5cdr_max_local_10 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 10)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 10% - local - max similarity
    
    bc5cdr_min_local_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 2)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 2% - local - max similarity

    bc5cdr_min_local_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 5)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 5% - local - max similarity
    
    bc5cdr_min_local_10 = df[
            (df['method'] == "cosiner")
          & (df['dataset'] == 'bc5cdr')
          & (df['scenario'] == 10)
          & (df["budget"] == 0)
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC5CDR - 10% - local - max similarity
    
    bc2gm_max_global_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 2)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 2% - global - max similarity

    bc2gm_max_global_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 5)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 5% - global - max similarity
    
    bc2gm_max_global_10 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 10)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 10% - global - max similarity
    
    bc2gm_min_global_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 2)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 2% - global - max similarity

    bc2gm_min_global_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 5)
          & (df["budget"] != 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 5% - global - max similarity
    
    bc2gm_min_global_10 = df[
            (df['method'] == "cosiner")
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 10)
          & (df["budget"] != 0)
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 10% - global - max similarity
    
    bc2gm_max_local_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 2)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 2% - local - max similarity

    bc2gm_max_local_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 5)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 5% - local - max similarity
    
    bc2gm_max_local_10 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 10)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "max")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 10% - local - max similarity
    
    bc2gm_min_local_2 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 2)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 2% - local - max similarity

    bc2gm_min_local_5 = df[
            (df['method'] == "cosiner") 
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 5)
          & (df["budget"] == 0) 
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 5% - local - max similarity
    
    bc2gm_min_local_10 = df[
            (df['method'] == "cosiner")
          & (df['dataset'] == 'bc2gm')
          & (df['scenario'] == 10)
          & (df["budget"] == 0)
          & (df["max_min_similarity"] == "min")
          ].loc[ lambda d: d['f1'].apply(lambda x: x[0]).idxmax()] # BC2GM - 10% - local - max similarity
    

    data = {
    "Dataset size": ["2\%", "2\%", "2\%", "2\%", "5\%", "5\%", "5\%", "5\%", "10\%", "10\%", "10\%", "10\%"],
    "Similarity": ["Maximum", "Minimum", "Maximum", "Minimum"]*3,
    "Strategy": ["Global", "Global", "Local", "Local"]*3,
    "NCBI Disease": [f"{ncbi_max_global_2['f1'][0]:.3f} $\pm$ {ncbi_max_global_2['f1'][1]:.3f}",
                     f"{ncbi_min_global_2['f1'][0]:.3f} $\pm$ {ncbi_min_global_2['f1'][1]:.3f}",
                     f"{ncbi_max_local_2['f1'][0]:.3f} $\pm$ {ncbi_max_local_2['f1'][1]:.3f}",
                     f"{ncbi_min_local_2['f1'][0]:.3f} $\pm$ {ncbi_min_local_2['f1'][1]:.3f}",
                     f"{ncbi_max_global_5['f1'][0]:.3f} $\pm$ {ncbi_max_global_5['f1'][1]:.3f}",
                     f"{ncbi_min_global_5['f1'][0]:.3f} $\pm$ {ncbi_min_global_5['f1'][1]:.3f}",
                     f"{ncbi_max_local_5['f1'][0]:.3f} $\pm$ {ncbi_max_local_5['f1'][1]:.3f}",
                     f"{ncbi_min_local_5['f1'][0]:.3f} $\pm$ {ncbi_min_local_5['f1'][1]:.3f}",
                     f"{ncbi_max_global_10['f1'][0]:.3f} $\pm$ {ncbi_max_global_10['f1'][1]:.3f}",
                     f"{ncbi_min_global_10['f1'][0]:.3f} $\pm$ {ncbi_min_global_10['f1'][1]:.3f}",
                     f"{ncbi_max_local_10['f1'][0]:.3f} $\pm$ {ncbi_max_local_10['f1'][1]:.3f}",
                     f"{ncbi_min_local_10['f1'][0]:.3f} $\pm$ {ncbi_min_local_10['f1'][1]:.3f}",
                    ],
    "BC5CDR": [f"{bc5cdr_max_global_2['f1'][0]:.3f} $\pm$ {bc5cdr_max_global_2['f1'][1]:.3f}",
               f"{bc5cdr_min_global_2['f1'][0]:.3f} $\pm$ {bc5cdr_min_global_2['f1'][1]:.3f}",
               f"{bc5cdr_max_local_2['f1'][0]:.3f} $\pm$ {bc5cdr_max_local_2['f1'][1]:.3f}",
               f"{bc5cdr_min_local_2['f1'][0]:.3f} $\pm$ {bc5cdr_min_local_2['f1'][1]:.3f}",
               f"{bc5cdr_max_global_5['f1'][0]:.3f} $\pm$ {bc5cdr_max_global_5['f1'][1]:.3f}",
               f"{bc5cdr_min_global_5['f1'][0]:.3f} $\pm$ {bc5cdr_min_global_5['f1'][1]:.3f}",
               f"{bc5cdr_max_local_5['f1'][0]:.3f} $\pm$ {bc5cdr_max_local_5['f1'][1]:.3f}",
               f"{bc5cdr_min_local_5['f1'][0]:.3f} $\pm$ {bc5cdr_min_local_5['f1'][1]:.3f}",
               f"{bc5cdr_max_global_10['f1'][0]:.3f} $\pm$ {bc5cdr_max_global_10['f1'][1]:.3f}",
               f"{bc5cdr_min_global_10['f1'][0]:.3f} $\pm$ {bc5cdr_min_global_10['f1'][1]:.3f}",
               f"{bc5cdr_max_local_10['f1'][0]:.3f} $\pm$ {bc5cdr_max_local_10['f1'][1]:.3f}",
               f"{bc5cdr_min_local_10['f1'][0]:.3f} $\pm$ {bc5cdr_min_local_10['f1'][1]:.3f}",
            ],

    "BC2GM": [f"{bc2gm_max_global_2['f1'][0]:.3f} $\pm$ {bc2gm_max_global_2['f1'][1]:.3f}",
              f"{bc2gm_min_global_2['f1'][0]:.3f} $\pm$ {bc2gm_min_global_2['f1'][1]:.3f}",
              f"{bc2gm_max_local_2['f1'][0]:.3f} $\pm$ {bc2gm_max_local_2['f1'][1]:.3f}",
              f"{bc2gm_min_local_2['f1'][0]:.3f} $\pm$ {bc2gm_min_local_2['f1'][1]:.3f}",
              f"{bc2gm_max_global_5['f1'][0]:.3f} $\pm$ {bc2gm_max_global_5['f1'][1]:.3f}",
              f"{bc2gm_min_global_5['f1'][0]:.3f} $\pm$ {bc2gm_min_global_5['f1'][1]:.3f}",
              f"{bc2gm_max_local_5['f1'][0]:.3f} $\pm$ {bc2gm_max_local_5['f1'][1]:.3f}",
              f"{bc2gm_min_local_5['f1'][0]:.3f} $\pm$ {bc2gm_min_local_5['f1'][1]:.3f}",
              f"{bc2gm_max_global_10['f1'][0]:.3f} $\pm$ {bc2gm_max_global_10['f1'][1]:.3f}",
              f"{bc2gm_min_global_10['f1'][0]:.3f} $\pm$ {bc2gm_min_global_10['f1'][1]:.3f}",
              f"{bc2gm_max_local_10['f1'][0]:.3f} $\pm$ {bc2gm_max_local_10['f1'][1]:.3f}",
              f"{bc2gm_min_local_10['f1'][0]:.3f} $\pm$ {bc2gm_min_local_10['f1'][1]:.3f}",
    ],
    }

    df = pd.DataFrame(data)

    data_original = [
    # size, similarity, strategy, NCBI, BC5CDR, BC2GM
    (2, "Maximum", "Global", 0.688, 0.830, 0.658),
    (2, "Minimum", "Global", 0.683, 0.823, 0.652),
    (2, "Maximum", "Local",  0.689, 0.832, 0.665),
    (2, "Minimum", "Local",  0.692, 0.824, 0.659),

    (5, "Maximum", "Global", 0.765, 0.858, 0.717),
    (5, "Minimum", "Global", 0.756, 0.853, 0.713),
    (5, "Maximum", "Local",  0.760, 0.863, 0.726),
    (5, "Minimum", "Local",  0.764, 0.860, 0.714),

    (10, "Maximum", "Global", 0.807, 0.880, 0.760),
    (10, "Minimum", "Global", 0.807, 0.873, 0.761),
    (10, "Maximum", "Local",  0.816, 0.860, 0.767),
    (10, "Minimum", "Local",  0.807, 0.876, 0.760),
    ]

    df_original = pd.DataFrame(data_original, columns=["Dataset size", "Similarity", "Strategy", "NCBI Disease", "BC5CDR", "BC2GM"])

    data_new = [
    # size, similarity, strategy, NCBI, BC5CDR, BC2GM
    (2, "Maximum", "Global", ncbi_max_global_2['f1'][0], bc5cdr_max_global_2['f1'][0], bc2gm_max_global_2['f1'][0]),
    (2, "Minimum", "Global", ncbi_min_global_2['f1'][0], bc5cdr_min_global_2['f1'][0], bc2gm_min_global_2['f1'][0]),
    (2, "Maximum", "Local",  ncbi_max_local_2['f1'][0], bc5cdr_max_local_2['f1'][0], bc2gm_max_local_2['f1'][0]),
    (2, "Minimum", "Local",  ncbi_min_local_2['f1'][0], bc5cdr_min_local_2['f1'][0], bc2gm_min_local_2['f1'][0]),

    (5, "Maximum", "Global", ncbi_max_global_5['f1'][0], bc5cdr_max_global_5['f1'][0], bc2gm_max_global_5['f1'][0]),
    (5, "Minimum", "Global", ncbi_min_global_5['f1'][0], bc5cdr_min_global_5['f1'][0], bc2gm_min_global_5['f1'][0]),
    (5, "Maximum", "Local",  ncbi_max_local_5['f1'][0], bc5cdr_max_local_5['f1'][0], bc2gm_max_local_5['f1'][0]),
    (5, "Minimum", "Local",  ncbi_min_local_5['f1'][0], bc5cdr_min_local_5['f1'][0], bc2gm_min_local_5['f1'][0]),

    (10, "Maximum", "Global", ncbi_max_global_10['f1'][0], bc5cdr_max_global_10['f1'][0], bc2gm_max_global_10['f1'][0]),
    (10, "Minimum", "Global", ncbi_min_global_10['f1'][0], bc5cdr_min_global_10['f1'][0], bc2gm_min_global_10['f1'][0]),
    (10, "Maximum", "Local",  ncbi_max_local_10['f1'][0], bc5cdr_max_local_10['f1'][0], bc2gm_max_local_10['f1'][0]),
    (10, "Minimum", "Local",  ncbi_min_local_10['f1'][0], bc5cdr_min_local_10['f1'][0], bc2gm_min_local_10['f1'][0]),
    ]

    df_new = pd.DataFrame(data_new, columns=["Dataset size", "Similarity", "Strategy", "NCBI Disease", "BC5CDR", "BC2GM"])

    results = []
    datasets = ["NCBI Disease", "BC5CDR", "BC2GM"]
    techniques = df_original[['Similarity', 'Strategy']].drop_duplicates().values.tolist()
    
    for dataset in datasets:
        for sim, strat in techniques:
            valsA = df_original[(df_original['Similarity'] == sim) & (df_original['Strategy'] == strat)][dataset].values
            valsB = df_new[(df_new['Similarity'] == sim) & (df_new['Strategy'] == strat)][dataset].values
            
            if len(valsA) == len(valsB) and len(valsA) == 3:
                pearson_corr = pearsonr(valsA, valsB)[0]
                spearman_corr = spearmanr(valsA, valsB)[0]
                results.append({
                    "Dataset": dataset,
                    "Similarity": sim,
                    "Strategy": strat,
                    "Pearson": pearson_corr,
                    "Spearman": spearman_corr
                })
    
    correlations = pd.DataFrame(results)

    # Group by dataset size for multirow
    latex_lines = []
    for size, group in df.groupby("Dataset size", sort=False):
        group_latex = group.drop(columns="Dataset size").to_latex(
            index=False, escape=False, header=False
        ).splitlines()[3:-2]  # strip LaTeX table environment
        group_latex[0] = f"\\multirow{{{len(group)}}}{{*}}{{{size}}} & " + group_latex[0]
        for i in range(1, len(group_latex)):
            group_latex[i] = " & " + group_latex[i]
        latex_lines.extend(group_latex)
        latex_lines.append("\\midrule")

    # Wrap into final LaTeX table
    latex_table = r"""
    \begin{table}
    \footnotesize
    \centering
    \caption{Comparative results between COSINER techniques with their best budget.}
    \begin{tabular}{@{}cp{0.15\textwidth}p{0.12\textwidth}lll@{}}
    \toprule
    \textbf{Dataset size} & \textbf{Similarity} & \textbf{Strategy} &
    \textbf{NCBI Disease} & \textbf{BC5CDR} & \textbf{BC2GM} \\ \midrule
    """ + "\n".join(latex_lines[:-1]) + r"""
    \bottomrule
    \end{tabular}
    \label{tab:methods_comp}
    \end{table}
    """
    return latex_table, correlations.to_latex(index=False, float_format="%.6f")

def convert_to_latex_t2(cosiner_df, melm_df, styleNER_df, baseline_df):

        data = {
        "NCBI Disease": {"F1": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
                        ],
                        "Precision": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
                        ],
                        "Recall": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        ]
        },

        "BC5CDR": {"F1": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
                        ],
                        "Precision": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
                        ],
                        "Recall": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        ]
        },
        "BC2GM": {"F1": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2)]['f1'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5)]['f1'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10)]['f1'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10)]['f1'].to_numpy()[0][1]:.3f}",
                        ],
                        "Precision": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2)]['precision'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5)]['precision'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10)]['precision'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10)]['precision'].to_numpy()[0][1]:.3f}",
                        ],
                        "Recall": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2)]['recall'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5)]['recall'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10)]['recall'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10)]['recall'].to_numpy()[0][1]:.3f}",
        ]
        },
        }

        methods = ["No Augmentation", "No Augmentation (BioBERT)", "MR", "LwTR", "SR", "MELM", "style_NER", "COSINER (ours)"]
        table_2 = dict_to_latex_table_2(data, methods)

        data_original = [
             (2, "No Augmentation", 0.430, 0.628, 0.510),
             (2, "No Augmentation (BioBERT)", 0.651, 0.792, 0.644),
             (2, "MR", 0.666, 0.813, 0.640),
             (2, "LwTR", 0.677, 0.828, 0.642),
             (2, "SR", 0.692, 0.813, 0.662),
             (2, "MELM", 0.578, 0.754, 0.566),
             (2, "style\_NER", 0.581, 0.752, 0.581),
             (2, "COSINER (ours)", 0.689, 0.832, 0.665),

             (5, "No Augmentation", 0.621, 0.757, 0.612),
             (5, "No Augmentation (BioBERT)", 0.735, 0.850, 0.711),
             (5, "MR", 0.743, 0.849, 0.713),
             (5, "LwTR", 0.743, 0.860, 0.699),
             (5, "SR", 0.758, 0.858, 0.719),
             (5, "MELM", 0.678, 0.800, 0.629),
             (5, "style\_NER", 0.687, 0.805, 0.640),
             (5, "COSINER (ours)", 0.760, 0.863, 0.726),

             (10, "No Augmentation", 0.712, 0.804, 0.669),
             (10, "No Augmentation (BioBERT)", 0.791, 0.875, 0.759),
             (10, "MR", 0.794, 0.874, 0.754),
             (10, "LwTR", 0.789, 0.882, 0.741),
             (10, "SR", 0.803, 0.883, 0.763),
             (10, "MELM", 0.740, 0.841, 0.685),
             (10, "style\_NER", 0.745, 0.838, 0.694),
             (10, "COSINER (ours)", 0.816, 0.882, 0.767)
        ]

        data_new = []
        for i, method in enumerate(methods):
                data_new.append((2,  method, float(data["NCBI Disease"]["F1"][i].split()[0]), float(data["BC5CDR"]["F1"][i].split()[0]), float(data["BC2GM"]["F1"][i].split()[0])))
                data_new.append((5,  method, float(data["NCBI Disease"]["F1"][i+8].split()[0]), float(data["BC5CDR"]["F1"][i+8].split()[0]), float(data["BC2GM"]["F1"][i+8].split()[0])))
                data_new.append((10, method, float(data["NCBI Disease"]["F1"][i+16].split()[0]), float(data["BC5CDR"]["F1"][i+16].split()[0]), float(data["BC2GM"]["F1"][i+16].split()[0])))

        df_original = pd.DataFrame(data_original, columns=["Dataset size", "Method", "NCBI Disease", "BC5CDR", "BC2GM"])
        df_new = pd.DataFrame(data_new, columns=["Dataset size", "Method", "NCBI Disease", "BC5CDR", "BC2GM"])
        print(df_original)
        print(df_new)

        results = []
        datasets = ["NCBI Disease", "BC5CDR", "BC2GM"]
        techniques = df_original['Method'].drop_duplicates().values.tolist()

        for dataset in datasets:
                for method in techniques:
                        valsA = df_original[(df_original['Method'] == method)][dataset].values
                        valsB = df_new[(df_new['Method'] == method)][dataset].values
                        if len(valsA) == len(valsB) and len(valsA) == 3:
                                pearson_corr = pearsonr(valsA, valsB)[0]
                                spearman_corr = spearmanr(valsA, valsB)[0]
                                results.append({
                                "Dataset": dataset,
                                "Method": method,
                                "Pearson": pearson_corr,
                                "Spearman": spearman_corr
                                })
    
        correlations = pd.DataFrame(results)
        print(correlations)
        return table_2, correlations.to_latex(index=False, float_format="%.6f")


def dict_to_latex_table_2(data, methods):
    metrics = ["F1", "Precision", "Recall"]
    size = ["2\%", "5\%", "10\%"]
    datasets = list(data.keys())

    rows = []
    for i, method in enumerate(methods*3):
        row_values = []
        if i % len(methods) == 0:
                rows.append(r"\midrule")
        for ds in datasets:
            for metric in metrics:
                row_values.append(data[ds][metric][i])
        if i % len(methods) == 0:
                s = size[int(i/len(methods))]
                row = r"\multirow{8}{*}{" + s + "} & " + method + " & " + " & ".join(row_values) + " \\\\"
        else:
                row = "&" + method + " & " + " & ".join(row_values) + " \\\\"
        rows.append(row)

    table = (
        r"""\begin{table}
        \footnotesize
        \centering
        \makegapedcells
        \caption{Comparative results between the local augmentation strategy with maximum similarity technique and baselines.}
        \scalebox{0.73}{\rotatebox{90}{\begin{tabular}{cllll|lll|lll}
        \toprule
        \textbf{Dataset size} & \multicolumn{1}{c}{\textbf{Method}} & \multicolumn{3}{c}{\textbf{NCBI-Disease}}                                                                                            & \multicolumn{3}{c}{\textbf{BC5CDR}}                                                                                                  & \multicolumn{3}{c}{\textbf{BC2GM}}                                                                                                   \\\midrule
        \multicolumn{1}{l}{}  &                                     & \multicolumn{1}{c}{F1}                     & \multicolumn{1}{c}{Precision}              & \multicolumn{1}{c}{Recall}                 & \multicolumn{1}{c}{F1}                     & \multicolumn{1}{c}{Precision}              & \multicolumn{1}{c}{Recall}                 & \multicolumn{1}{c}{F1}                     & \multicolumn{1}{c}{Precision}              & \multicolumn{1}{c}{Recall}                 \\ """
        + "\n".join(rows)
        + r"""\bottomrule
        \end{tabular}}}
        \label{tab:baselines_comp}
        \end{table}"""
    )

    return table

def convert_to_latex_aug(cosiner_df, melm_df, styleNER_df, baseline_df):
    data = {"NCBI Disease": 
                {"time": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][1]:.3f}",


        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'ncbi') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'ncbi') & (melm_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'ncbi') & (styleNER_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'ncbi') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][1]:.3f}",
                        ],
                },

        "BC5CDR": {"time": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc5cdr') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc5cdr') & (melm_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc5cdr') & (styleNER_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc5cdr') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][1]:.3f}",
            ],
        },
                    
        "BC2GM": {"time": [
        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 2) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 5) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][1]:.3f}",

        f"{baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'bert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'biobert') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'mr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'lwtr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {baseline_df[(baseline_df['method'] == 'sr') & (baseline_df['dataset'] == 'bc2gm') & (baseline_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {melm_df[(melm_df['dataset'] == 'bc2gm') & (melm_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {styleNER_df[(styleNER_df['dataset'] == 'bc2gm') & (styleNER_df['scenario'] == 10)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 2)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 5)]['time'].to_numpy()[0][1]:.3f}",
        f"{cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][0]:.3f} $\pm$ {cosiner_df[(cosiner_df['dataset'] == 'bc2gm') & (cosiner_df['scenario'] == 10) & (cosiner_df['exr'] == 10)]['time'].to_numpy()[0][1]:.3f}",
                ],
            }            
        }

    methods = ["No Augmentation", "No Augmentation (BioBERT)", "MR", "LwTR", "SR", "MELM", "style\_NER", "COSINER (small)", "COSINER (medium)", "COSINER (large)"]
    size = ["2\%", "5\%", "10\%"]
    datasets = list(data.keys())

    rows = []
    for i, method in enumerate(methods*3):
        row_values = []
        if i % len(methods) == 0:
                rows.append(r"\midrule")
        for ds in datasets:
            row_values.append(data[ds]["time"][i])
        if i % len(methods) == 0:
                s = size[int(i/len(methods))]
                row = r"\multirow{10}{*}{" + s + "} & " + method + " & " + " & ".join(row_values) + " \\\\"
        else:
                row = "&" + method + " & " + " & ".join(row_values) + " \\\\"
        rows.append(row)

    latex_table = r"""
    \begin{table}
    \footnotesize
    \centering
    \caption{Run times (s) for data augmentation with 95\% confidence intervals. Comparison with baselines and budgets.}
    \label{tab:tempi-aug}
    \rotatebox{90}{\begin{tabular}{@{}cp{0.4\textwidth}p{0.3\textwidth}p{0.2\textwidth}p{0.2\textwidth}@{}}
    \toprule
    \textbf{Dataset size} & \textbf{Method} & \textbf{NCBI Disease} & \textbf{BC5CDR} & \textbf{BC2GM} \\\midrule
    """ + "\n".join(rows) + r"""\bottomrule
    \end{tabular}}
    \end{table}
    """

    print(latex_table)
    return latex_table



