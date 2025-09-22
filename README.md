# COSINER Setup and Execution Guide

This guide provides step-by-step instructions for setting up and running COSINER experiments. Please follow all steps carefully to ensure reproducible results.

## Prerequisites

Before beginning, ensure your system meets the following requirements:

- **Python**: Version 3.10 or higher ([Download Python](https://www.python.org/downloads/))
- **Git LFS**: Required for large file handling ([Installation guide](https://git-lfs.github.io/))
- **CUDA**: CUDA-compatible GPU with appropriate drivers for GPU acceleration
- **Operating System**: Linux, macOS, or Windows with PowerShell/Command Prompt
- **Disk Space**: At least ???GB of free space (including datasets and model checkpoints)
- **Memory**: Minimum ???GB RAM recommended

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
