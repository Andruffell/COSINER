# COSINER Setup and Execution Guide
## Requirements

Python ≥ 3.10

git-lfs

`venv` module (comes with Python standard library)

CUDA-compatible GPU (for GPU acceleration)


## 1. Clone the repository
Include all submodules:

    git clone --recursive https://github.com/Andruffell/COSINER.git
    cd COSINER

## 2. Create and activate the virtual environment

Create the venv:

`python -m venv COSINER`

Activate it depending on your OS:
**macOS / Linux**:

`source COSINER/bin/activate`

**Windows (cmd.exe)**:

`COSINER/Scripts/activate`

**Windows (PowerShell)**:

`./COSINER/Scripts/Activate.ps1`

After activation, your prompt should show (COSINER).

## 3. Install dependencies

    pip install --upgrade pip
    pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

## 4. Run COSINER experiments
COSINER experiments:

`./experiments.sh`

Baselines experiments:

`./experiments_baselines.sh`


# Common problems:
`./experiments.sh` or `./experiments_baselines.sh` are not running

## Possible fix:
Give execution privileges to the shell scripts:

    chmod +x experiments.sh 
    chmod +x experiments_baselines.sh

Be sure that the virtual environment name corresponds to the one suggested (COSINER).




