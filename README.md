# COSINER Setup and Execution Guide

This guide provides step-by-step instructions for setting up and running COSINER experiments. Please follow all steps carefully to ensure reproducible results.

## Prerequisites

Before beginning, ensure your system meets the following requirements:

- **Python**: Version 3.10 or higher ([Download Python](https://www.python.org/downloads/))
- **Git LFS**: Required for large file handling ([Installation guide](https://git-lfs.github.io/))
- **CUDA**: CUDA-compatible GPU with appropriate drivers for GPU acceleration
- **Operating System**: Linux, macOS, or Windows with PowerShell/Command Prompt
- **Disk Space**: At least 10 GB of free space (including datasets and model checkpoints)
- **Memory**: Minimum 32 GB RAM recommended

## Installation

### 1. Repository Setup

Clone the repository with all submodules:

```bash
git clone --recursive https://github.com/Andruffell/COSINER.git
cd COSINER
```

**Note**: The `--recursive` flag is essential as it includes all necessary submodules and dependencies.

### 2. Virtual Environment Setup

Create an isolated Python environment to avoid dependency conflicts:

```bash
python -m venv COSINER
```

Activate the virtual environment based on your operating system:

**Linux/macOS:**
```bash
source COSINER/bin/activate
```

**Windows Command Prompt:**
```cmd
COSINER\Scripts\activate.bat
```

**Windows PowerShell:**
```powershell
.\COSINER\Scripts\Activate.ps1
```

After successful activation, your terminal prompt should display `(COSINER)` at the beginning.

### 3. Dependency Installation

Upgrade pip and install all required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
```

**Verification**: Confirm successful installation by checking key packages:
```bash
python -c "import torch; print(f'PyTorch version: {torch.__version__}')"
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```

## Running Experiments

### COSINER Experiments

Execute the main COSINER experiments:

```bash
./experiments.sh
```

### Baseline Comparisons

Run baseline experiments for comparison:

```bash
./experiments_baselines.sh
```

## Troubleshooting

### Permission Issues

If shell scripts fail to execute with permission errors:

```bash
chmod +x experiments.sh experiments_baselines.sh
```

### Virtual Environment Issues

Ensure you're using the correct virtual environment:

1. Verify the environment is activated (check for `(COSINER)` in your prompt)
2. If deactivated, reactivate using the commands in Section 2
3. Confirm the environment name matches exactly: `COSINER`

### CUDA Issues

If GPU acceleration is not working:

1. Verify CUDA installation: `nvidia-smi`
2. Check PyTorch CUDA compatibility: `python -c "import torch; print(torch.cuda.is_available())"`
3. Ensure CUDA drivers match PyTorch requirements

### Memory Issues

If encountering out-of-memory errors:

- Reduce batch size in configuration files
- Close other GPU-intensive applications
- Consider using CPU-only mode for initial testing

### Package Installation Issues

If pip installation fails:

1. Ensure pip is up to date: `pip install --upgrade pip`
2. Try installing packages individually to identify problematic dependencies
3. Clear pip cache: `pip cache purge`

# Citation

If you use COSINER in your research, please cite the original papers and relevant resources:

## Original papers
```
@article{bartolini2023data,
  title={Data augmentation via context similarity: An application to biomedical Named Entity Recognition},
  author={Bartolini, Ilaria and Moscato, Vincenzo and Postiglione, Marco and Sperl{\`\i}, Giancarlo and Vignali, Andrea},
  journal={Information Systems},
  volume={119},
  pages={102291},
  year={2023},
  publisher={Elsevier}
}

@inproceedings{bartolini2022cosiner,
  title={COSINER: Context similarity data augmentation for named entity recognition},
  author={Bartolini, Ilaria and Moscato, Vincenzo and Postiglione, Marco and Sperl{\`\i}, Giancarlo and Vignali, Andrea},
  booktitle={International Conference on Similarity Search and Applications},
  pages={11--24},
  year={2022},
  organization={Springer}
}
```
## Datasets
```
@article{ncbi,
          author = {Dogan, Rezarta Islamaj and Leaman, Robert and Lu, Zhiyong},
          title = {NCBI Disease Corpus},
          year = {2014},
          issue_date = {February 2014},
          publisher = {Elsevier Science},
          address = {San Diego, CA, USA},
          volume = {47},
          number = {C},
          issn = {1532-0464},
          journal = {J. of Biomedical Informatics},
          month = {feb},
          pages = {1–10},
          numpages = {10}}

@article{article,
          author = {Li, Jiao and Sun, Yueping and Johnson, Robin and Sciaky, Daniela and Wei, Chih-Hsuan and Leaman, Robert and Davis, Allan Peter and Mattingly, Carolyn and Wiegers, Thomas and lu, Zhiyong},
          year = {2016},
          month = {05},
          pages = {baw068},
          title = {BioCreative V CDR task corpus: a resource for chemical disease relation extraction},
          volume = {2016},
          journal = {Database},
          doi = {10.1093/database/baw068}
          }

@article{bc2gm,
          author = {Smith, Larry and Tanabe, Lorraine and Ando, Rie and Kuo, Cheng-Ju and Chung, I-Fang and Hsu, Chun-Nan and Lin, Yu-Shi and Klinger, Roman and Friedrich, Christoph and Ganchev, Kuzman and Torii, Manabu and Liu, Hongfang and Haddow, Barry and Struble, Craig and Povinelli, Richard and Vlachos, Andreas and Baumgartner Jr, William and Hunter, Lawrence and Carpenter, Bob and Wilbur, W.},
          year = {2008},
          month = {09},
          pages = {S2},
          title = {Overview of BioCreative II gene mention recognition},
          volume = {9 Suppl 2},
          journal = {Genome biology},
          doi = {10.1186/gb-2008-9-s2-s2}
          }

@article{bc5cdr,
          author = {Li, Jiao and Sun, Yueping and Johnson, Robin and Sciaky, Daniela and Wei, Chih-Hsuan and Leaman, Robert and Davis, Allan Peter and Mattingly, Carolyn and Wiegers, Thomas and lu, Zhiyong},
          year = {2016},
          month = {05},
          pages = {baw068},
          title = {BioCreative V CDR task corpus: a resource for chemical disease relation extraction},
          volume = {2016},
          journal = {Database},
          doi = {10.1093/database/baw068}
          }

@article{chemdner,
  title        = {The CHEMDNER corpus of chemicals and drugs and its annotation principles},
  author       = {
    Krallinger, Martin and Rabal, Obdulia and Leitner, Florian and Vazquez,
    Miguel and Salgado, David and Lu, Zhiyong and Leaman, Robert and Lu, Yanan
    and Ji, Donghong and Lowe, Daniel M. and Sayle, Roger A. and
    Batista-Navarro, Riza Theresa and Rak, Rafal and Huber, Torsten and
    Rockt{"a}schel, Tim and Matos, S{'e}rgio and Campos, David and Tang,
    Buzhou and Xu, Hua and Munkhdalai, Tsendsuren and Ryu, Keun Ho and Ramanan,
    S. V. and Nathan, Senthil and {{Z}}itnik, Slavko and Bajec, Marko and
    Weber, Lutz and Irmer, Matthias and Akhondi, Saber A. and Kors, Jan A. and
    Xu, Shuo and An, Xin and Sikdar, Utpal Kumar and Ekbal, Asif and Yoshioka,
    Masaharu and Dieb, Thaer M. and Choi, Miji and Verspoor, Karin and Khabsa,
    Madian and Giles, C. Lee and Liu, Hongfang and Ravikumar, Komandur
    Elayavilli and Lamurias, Andre and Couto, Francisco M. and Dai, Hong-Jie
    and Tsai, Richard Tzong-Han and Ata, Caglar and Can, Tolga and Usi{'e},
    Anabel and Alves, Rui and Segura-Bedmar, Isabel and Mart{'i}nez, Paloma
    and Oyarzabal, Julen and Valencia, Alfonso
  },
  year         = 2015,
  month        = {Jan},
  day          = 19,
  journal      = {Journal of Cheminformatics},
  volume       = 7,
  number       = 1,
  pages        = {S2},
  doi          = {10.1186/1758-2946-7-S1-S2},
  issn         = {1758-2946},
  url          = {https://doi.org/10.1186/1758-2946-7-S1-S2},
}

@inproceedings{jnlpba,
          title = "Introduction to the Bio-entity Recognition Task at {JNLPBA}",
          author = "Collier, Nigel  and
            Kim, Jin-Dong",
          booktitle = "Proceedings of the International Joint Workshop on Natural Language Processing in Biomedicine and its Applications ({NLPBA}/{B}io{NLP})",
          month = aug # " 28th and 29th",
          year = "2004",
          address = "Geneva, Switzerland",
          publisher = "COLING",
          url = "https://aclanthology.org/W04-1213",
          pages = "73--78",
          }
```

# License
This project is licensed under the MIT License.
