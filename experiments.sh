#!/usr/bin/env bash
set -e

VENV_DIR="COSINER"

if [[ -f "$VENV_DIR/Scripts/python.exe" ]]; then
    PYTHON_EXEC="$VENV_DIR/Scripts/python.exe"
elif [[ -f "$VENV_DIR/bin/python" ]]; then
    PYTHON_EXEC="$VENV_DIR/bin/python"
else
    echo "Python executable not found in $VENV_DIR (checked both Windows and Linux paths)"
    exit 1
fi

datasets=("ncbi" "bc5cdr" "bc2gm")
percentages=(2 5 10)
exr=(2 5 10)
budget=0
reverse=(0 1)
seeds=(100 200 300 400 500)

declare -A lengths
# NCBI
lengths["ncbi_2"]=108
lengths["ncbi_5"]=271
lengths["ncbi_10"]=542
# BC5CDR
lengths["bc5cdr_2"]=91
lengths["bc5cdr_5"]=228
lengths["bc5cdr_10"]=456
# BC2GM
lengths["bc2gm_2"]=251
lengths["bc2gm_5"]=628
lengths["bc2gm_10"]=1257


total=$(( (2 * ${#datasets[@]} * ${#percentages[@]} * ${#seeds[@]} * ${#exr[@]} * ${#reverse[@]}) ))
count=0

echo "Total experiments to check: $total"
echo "-----------------------------------"


for dataset in "${datasets[@]}"; do
    for pct in "${percentages[@]}"; do
        length=${lengths["${dataset}_${pct}"]}
        for e in "${exr[@]}"; do
            for r in "${reverse[@]}"; do
                for seed in "${seeds[@]}"; do
                    count=$((count + 1))

                    result_file="./results/cosiner/${dataset}/${dataset}_${length}_${e}_${budget}_${reverse}_${seed}.xlsx"

                    echo -n "[$count/$total]"

                    if [[ -f "$result_file" ]]; then
                        echo "SKIP (exists): $result_file"
                        continue
                    fi

                    echo "RUN: COSINER | $dataset | ${pct}% | seed=$seed"
                    "$PYTHON_EXEC" main_cosiner.py \
                        -dataset "data/${dataset}.hf" \
                        -length "$length" \
                        -exr "$e" \
                        -budget 0 \
                        -reverse "$r" \
                        -seed "$seed"
                done
            done
        done
    done
done

echo "-----------------------------------"
echo "COSINER local experiments processed"
echo "COSINER global starting"

exr=10
budget=(100 300 500)

for dataset in "${datasets[@]}"; do
    for pct in "${percentages[@]}"; do
        length=${lengths["${dataset}_${pct}"]}
        for b in "${budget[@]}"; do
            for r in "${reverse[@]}"; do
                for seed in "${seeds[@]}"; do
                    count=$((count + 1))

                    result_file="./results/cosiner/${dataset}/${dataset}_${length}_${exr}_${b}_${reverse}_${seed}.xlsx"

                    echo -n "[$count/$total]"

                    if [[ -f "$result_file" ]]; then
                        echo "SKIP (exists): $result_file"
                        continue
                    fi

                    echo "RUN: COSINER | $dataset | ${pct}% | seed=$seed"
                    "$PYTHON_EXEC" main_cosiner.py \
                        -dataset "data/${dataset}.hf" \
                        -length "$length" \
                        -exr 10 \
                        -budget "$b" \
                        -reverse "$r" \
                        -seed "$seed"
                done
            done
        done
    done
done

echo "-----------------------------------"
echo "All COSINER experiments processed"