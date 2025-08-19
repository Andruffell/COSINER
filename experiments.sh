#!/usr/bin/env bash
set -e

VENV_DIR="COSINER"

if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "win32" ]]; then
    PYTHON_EXEC="$VENV_DIR/Scripts/python.exe"
else
    PYTHON_EXEC="$VENV_DIR/bin/python"
fi

if [[ ! -f "$PYTHON_EXEC" ]]; then
    echo "Python executable not found at: $PYTHON_EXEC"
    exit 1
fi

#DATASET: NCBI
##FEW SHOT SCENARIO: 2% (108)
####STRATEGY: LOCAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 2 -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 2 -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 2 -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 2 -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 2 -budget 0 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 5  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 5  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 5  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 5  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 5  -budget 0 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 0 -reverse 0 -seed 500 

#####SIMILARITY: MIN 
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 2 -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 2 -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 2 -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 2 -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 2 -budget 0 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 5  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 5  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 5  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 5  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 5  -budget 0 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 0 -reverse 1 -seed 500 

####STRATEGY: GLOBAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10 -budget 100 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10 -budget 100 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10 -budget 100 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10 -budget 100 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10 -budget 100 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 300 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 300 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 300 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 300 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 300 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 500 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 500 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 500 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 500 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 500 -reverse 0 -seed 500 

#####SIMILARITY: MIN
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10 -budget 100 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10 -budget 100 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10 -budget 100 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10 -budget 100 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10 -budget 100 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 300 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 300 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 300 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 300 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 300 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 500 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 500 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 500 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 500 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 108 -exr 10  -budget 500 -reverse 1 -seed 500 





##FEW SHOT SCENARIO: 5% (271)
####STRATEGY: LOCAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 2 -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 2 -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 2 -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 2 -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 2 -budget 0 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 5  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 5  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 5  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 5  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 5  -budget 0 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 0 -reverse 0 -seed 500 

#####SIMILARITY: MIN 
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 2 -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 2 -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 2 -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 2 -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 2 -budget 0 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 5  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 5  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 5  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 5  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 5  -budget 0 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 0 -reverse 1 -seed 500 

####STRATEGY: GLOBAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10 -budget 100 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10 -budget 100 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10 -budget 100 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10 -budget 100 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10 -budget 100 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 300 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 300 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 300 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 300 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 300 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 500 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 500 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 500 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 500 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 500 -reverse 0 -seed 500 

#####SIMILARITY: MIN
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10 -budget 100 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10 -budget 100 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10 -budget 100 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10 -budget 100 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10 -budget 100 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 300 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 300 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 300 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 300 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 300 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 500 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 500 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 500 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 500 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 271 -exr 10  -budget 500 -reverse 1 -seed 500 






##FEW SHOT SCENARIO: 10% (542)
####STRATEGY: LOCAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 2 -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 2 -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 2 -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 2 -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 2 -budget 0 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 5  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 5  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 5  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 5  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 5  -budget 0 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 0 -reverse 0 -seed 500 

#####SIMILARITY: MIN 
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 2 -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 2 -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 2 -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 2 -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 2 -budget 0 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 5  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 5  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 5  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 5  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 5  -budget 0 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 0 -reverse 1 -seed 500 

####STRATEGY: GLOBAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10 -budget 100 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10 -budget 100 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10 -budget 100 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10 -budget 100 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10 -budget 100 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 300 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 300 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 300 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 300 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 300 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 500 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 500 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 500 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 500 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 500 -reverse 0 -seed 500 

#####SIMILARITY: MIN
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10 -budget 100 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10 -budget 100 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10 -budget 100 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10 -budget 100 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10 -budget 100 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 300 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 300 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 300 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 300 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 300 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 500 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 500 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 500 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 500 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/ncbi.hf -length 542 -exr 10  -budget 500 -reverse 1 -seed 500 





#BC5
##FEW SHOT SCENARIO: 2% (91)
####STRATEGY: LOCAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 2 -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 2 -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 2 -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 2 -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 2 -budget 0 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 5  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 5  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 5  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 5  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 5  -budget 0 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 0 -reverse 0 -seed 500 

#####SIMILARITY: MIN 
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 2 -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 2 -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 2 -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 2 -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 2 -budget 0 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 5  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 5  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 5  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 5  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 5  -budget 0 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 0 -reverse 1 -seed 500 

####STRATEGY: GLOBAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10 -budget 100 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10 -budget 100 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10 -budget 100 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10 -budget 100 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10 -budget 100 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 300 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 300 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 300 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 300 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 300 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 500 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 500 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 500 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 500 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 500 -reverse 0 -seed 500 

#####SIMILARITY: MIN
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10 -budget 100 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10 -budget 100 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10 -budget 100 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10 -budget 100 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10 -budget 100 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 300 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 300 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 300 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 300 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 300 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 500 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 500 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 500 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 500 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 91 -exr 10  -budget 500 -reverse 1 -seed 500 










##FEW SHOT SCENARIO: 5% (228)
####STRATEGY: LOCAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 2 -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 2 -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 2 -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 2 -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 2 -budget 0 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 5  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 5  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 5  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 5  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 5  -budget 0 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 0 -reverse 0 -seed 500 

#####SIMILARITY: MIN 
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 2 -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 2 -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 2 -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 2 -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 2 -budget 0 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 5  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 5  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 5  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 5  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 5  -budget 0 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 0 -reverse 1 -seed 500 

####STRATEGY: GLOBAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10 -budget 100 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10 -budget 100 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10 -budget 100 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10 -budget 100 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10 -budget 100 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 300 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 300 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 300 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 300 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 300 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 500 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 500 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 500 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 500 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 500 -reverse 0 -seed 500 

#####SIMILARITY: MIN
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10 -budget 100 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10 -budget 100 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10 -budget 100 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10 -budget 100 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10 -budget 100 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 300 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 300 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 300 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 300 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 300 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 500 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 500 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 500 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 500 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 228 -exr 10  -budget 500 -reverse 1 -seed 500 







##FEW SHOT SCENARIO: 10% (456)
####STRATEGY: LOCAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 2 -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 2 -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 2 -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 2 -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 2 -budget 0 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 5  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 5  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 5  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 5  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 5  -budget 0 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 0 -reverse 0 -seed 500 

#####SIMILARITY: MIN 
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 2 -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 2 -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 2 -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 2 -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 2 -budget 0 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 5  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 5  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 5  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 5  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 5  -budget 0 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 0 -reverse 1 -seed 500 

####STRATEGY: GLOBAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10 -budget 100 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10 -budget 100 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10 -budget 100 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10 -budget 100 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10 -budget 100 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 300 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 300 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 300 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 300 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 300 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 500 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 500 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 500 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 500 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 500 -reverse 0 -seed 500 

#####SIMILARITY: MIN
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10 -budget 100 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10 -budget 100 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10 -budget 100 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10 -budget 100 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10 -budget 100 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 300 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 300 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 300 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 300 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 300 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 500 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 500 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 500 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 500 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc5cdr.hf -length 456 -exr 10  -budget 500 -reverse 1 -seed 500 






#B2G
##FEW SHOT SCENARIO: 2% (251)
####STRATEGY: LOCAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 2 -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 2 -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 2 -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 2 -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 2 -budget 0 -reverse 0 -seed 500

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 5  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 5  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 5  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 5  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 5  -budget 0 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 0 -reverse 0 -seed 500 

#####SIMILARITY: MIN 
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 2 -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 2 -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 2 -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 2 -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 2 -budget 0 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 5  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 5  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 5  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 5  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 5  -budget 0 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 0 -reverse 1 -seed 500 

####STRATEGY: GLOBAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10 -budget 100 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10 -budget 100 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10 -budget 100 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10 -budget 100 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10 -budget 100 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 300 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 300 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 300 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 300 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 300 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 500 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 500 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 500 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 500 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 500 -reverse 0 -seed 500 

#####SIMILARITY: MIN
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10 -budget 100 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10 -budget 100 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10 -budget 100 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10 -budget 100 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10 -budget 100 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 300 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 300 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 300 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 300 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 300 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 500 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 500 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 500 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 500 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 251 -exr 10  -budget 500 -reverse 1 -seed 500 





##FEW SHOT SCENARIO: 5% (628)
####STRATEGY: LOCAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 2 -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 2 -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 2 -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 2 -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 2 -budget 0 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 5  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 5  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 5  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 5  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 5  -budget 0 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 0 -reverse 0 -seed 500 

#####SIMILARITY: MIN 
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 2 -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 2 -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 2 -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 2 -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 2 -budget 0 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 5  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 5  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 5  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 5  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 5  -budget 0 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 0 -reverse 1 -seed 500 

####STRATEGY: GLOBAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10 -budget 100 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10 -budget 100 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10 -budget 100 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10 -budget 100 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10 -budget 100 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 300 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 300 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 300 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 300 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 300 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 500 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 500 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 500 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 500 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 500 -reverse 0 -seed 500 

#####SIMILARITY: MIN
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10 -budget 100 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10 -budget 100 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10 -budget 100 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10 -budget 100 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10 -budget 100 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 300 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 300 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 300 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 300 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 300 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 500 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 500 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 500 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 500 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 628 -exr 10  -budget 500 -reverse 1 -seed 500 






##FEW SHOT SCENARIO: 10% (1257)
####STRATEGY: LOCAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 2 -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 2 -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 2 -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 2 -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 2 -budget 0 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 5  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 5  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 5  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 5  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 5  -budget 0 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 0 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 0 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 0 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 0 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 0 -reverse 0 -seed 500 

#####SIMILARITY: MIN 
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 2 -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 2 -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 2 -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 2 -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 2 -budget 0 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 5  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 5  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 5  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 5  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 5  -budget 0 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 0 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 0 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 0 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 0 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 0 -reverse 1 -seed 500 

####STRATEGY: GLOBAL
#####SIMILARITY: MAX
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10 -budget 100 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10 -budget 100 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10 -budget 100 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10 -budget 100 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10 -budget 100 -reverse 0 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 300 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 300 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 300 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 300 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 300 -reverse 0 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 500 -reverse 0 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 500 -reverse 0 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 500 -reverse 0 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 500 -reverse 0 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 500 -reverse 0 -seed 500 

#####SIMILARITY: MIN
######BUDGET: SMALL
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10 -budget 100 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10 -budget 100 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10 -budget 100 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10 -budget 100 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10 -budget 100 -reverse 1 -seed 500 

######BUDGET: MEDIUM
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 300 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 300 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 300 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 300 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 300 -reverse 1 -seed 500 

######BUDGET: LARGE
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 500 -reverse 1 -seed 100 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 500 -reverse 1 -seed 200 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 500 -reverse 1 -seed 300 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 500 -reverse 1 -seed 400 
"$PYTHON_EXEC" main_cosiner.py -dataset data/bc2gm.hf -length 1257 -exr 10  -budget 500 -reverse 1 -seed 500 

