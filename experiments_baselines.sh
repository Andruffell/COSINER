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

#### MELM
##### NCBI
###### 2%

"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 108 -seed 100 
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 108 -seed 200
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 108 -seed 300
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 108 -seed 400
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 108 -seed 500

###### 5%

"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 271 -seed 100 
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 271 -seed 200
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 271 -seed 300
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 271 -seed 400
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 271 -seed 500

###### 10%

"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 542 -seed 100 
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 542 -seed 200
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 542 -seed 300
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 542 -seed 400
"$PYTHON_EXEC" main_melm.py -dataset data/ncbi.hf -length 542 -seed 500

##### BC5CDR
###### 2%

"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 91 -seed 100 
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 91 -seed 200
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 91 -seed 300
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 91 -seed 400
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 91 -seed 500

###### 5%

"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 228 -seed 100 
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 228 -seed 200
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 228 -seed 300
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 228 -seed 400
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 228 -seed 500

###### 10%

"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 456 -seed 100 
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 456 -seed 200
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 456 -seed 300
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 456 -seed 400
"$PYTHON_EXEC" main_melm.py -dataset data/bc5cdr.hf -length 456 -seed 500

##### BC2GM
###### 2%

"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 251 -seed 100 
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 251 -seed 200
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 251 -seed 300
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 251 -seed 400
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 251 -seed 500

###### 5%

"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 628 -seed 100 
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 628 -seed 200
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 628 -seed 300
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 628 -seed 400
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 628 -seed 500

###### 10%

"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 1257 -seed 100 
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 1257 -seed 200
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 1257 -seed 300
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 1257 -seed 400
"$PYTHON_EXEC" main_melm.py -dataset data/bc2gm.hf -length 1257 -seed 500



#### style_NER
##### NCBI
###### 2%

"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 108 -seed 100 
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 108 -seed 200
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 108 -seed 300
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 108 -seed 400
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 108 -seed 500

###### 5%

"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 271 -seed 100 
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 271 -seed 200
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 271 -seed 300
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 271 -seed 400
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 271 -seed 500

###### 10%

"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 542 -seed 100 
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 542 -seed 200
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 542 -seed 300
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 542 -seed 400
"$PYTHON_EXEC" main_style_NER.py -dataset data/ncbi.hf -length 542 -seed 500

##### BC5CDR
###### 2%

"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 91 -seed 100 
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 91 -seed 200
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 91 -seed 300
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 91 -seed 400
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 91 -seed 500

###### 5%

"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 228 -seed 100 
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 228 -seed 200
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 228 -seed 300
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 228 -seed 400
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 228 -seed 500

###### 10%

"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 456 -seed 100 
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 456 -seed 200
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 456 -seed 300
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 456 -seed 400
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc5cdr.hf -length 456 -seed 500

##### BC2GM
###### 2%

"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 251 -seed 100 
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 251 -seed 200
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 251 -seed 300
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 251 -seed 400
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 251 -seed 500

###### 5%

"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 628 -seed 100 
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 628 -seed 200
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 628 -seed 300
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 628 -seed 400
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 628 -seed 500

###### 10%

"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 1257 -seed 100 
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 1257 -seed 200
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 1257 -seed 300
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 1257 -seed 400
"$PYTHON_EXEC" main_style_NER.py -dataset data/bc2gm.hf -length 1257 -seed 500



#### LWTR
##### NCBI
###### 2%

"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 108 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 108 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 108 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 108 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 108 -seed 500

###### 5%

"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 271 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 271 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 271 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 271 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 271 -seed 500

###### 10%

"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 542 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 542 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 542 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 542 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/ncbi.hf -length 542 -seed 500

##### BC5CDR
###### 2%

"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 91 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 91 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 91 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 91 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 91 -seed 500

###### 5%

"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 228 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 228 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 228 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 228 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 228 -seed 500

###### 10%

"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 456 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 456 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 456 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 456 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc5cdr.hf -length 456 -seed 500

##### BC2GM
###### 2%

"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 251 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 251 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 251 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 251 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 251 -seed 500

###### 5%

"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 628 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 628 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 628 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 628 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 628 -seed 500

###### 10%

"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 1257 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 1257 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 1257 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 1257 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline lwtr -dataset data/bc2gm.hf -length 1257 -seed 500



#### mr
##### NCBI
###### 2%

"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 108 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 108 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 108 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 108 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 108 -seed 500

###### 5%

"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 271 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 271 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 271 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 271 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 271 -seed 500

###### 10%

"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 542 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 542 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 542 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 542 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/ncbi.hf -length 542 -seed 500

##### BC5CDR
###### 2%

"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 91 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 91 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 91 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 91 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 91 -seed 500

###### 5%

"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 228 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 228 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 228 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 228 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 228 -seed 500

###### 10%

"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 456 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 456 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 456 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 456 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc5cdr.hf -length 456 -seed 500

##### BC2GM
###### 2%

"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 251 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 251 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 251 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 251 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 251 -seed 500

###### 5%

"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 628 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 628 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 628 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 628 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 628 -seed 500

###### 10%

"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 1257 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 1257 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 1257 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 1257 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline mr -dataset data/bc2gm.hf -length 1257 -seed 500



#### sr
##### NCBI
###### 2%

"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 108 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 108 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 108 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 108 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 108 -seed 500

###### 5%

"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 271 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 271 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 271 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 271 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 271 -seed 500

###### 10%

"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 542 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 542 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 542 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 542 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/ncbi.hf -length 542 -seed 500

##### BC5CDR
###### 2%

"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 91 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 91 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 91 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 91 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 91 -seed 500

###### 5%

"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 228 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 228 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 228 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 228 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 228 -seed 500

###### 10%

"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 456 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 456 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 456 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 456 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc5cdr.hf -length 456 -seed 500

##### BC2GM
###### 2%

"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 251 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 251 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 251 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 251 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 251 -seed 500

###### 5%

"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 628 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 628 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 628 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 628 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 628 -seed 500

###### 10%

"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 1257 -seed 100 
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 1257 -seed 200
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 1257 -seed 300
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 1257 -seed 400
"$PYTHON_EXEC" main_baseline.py -baseline sr -dataset data/bc2gm.hf -length 1257 -seed 500