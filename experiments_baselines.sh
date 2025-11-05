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

baselines=("bert" "biobert" "lwtr" "mr" "sr")
datasets=("ncbi" "bc5cdr" "bc2gm")
percentages=(2 5 10)
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


total=$(( (${#baselines[@]} * ${#datasets[@]} * ${#percentages[@]} * ${#seeds[@]}) + (2 * ${#datasets[@]} * ${#percentages[@]} * ${#seeds[@]}) ))
count=0

echo "Total experiments to check: $total"
echo "-----------------------------------"

for baseline in "${baselines[@]}"; do
    for dataset in "${datasets[@]}"; do
        for pct in "${percentages[@]}"; do
            length=${lengths["${dataset}_${pct}"]}
            for seed in "${seeds[@]}"; do
                count=$((count + 1))

                result_file="./results/baselines/${dataset}/${dataset}_${baseline}_${length}_${seed}.xlsx"

                echo -n "[$count/$total]"

                if [[ -f "$result_file" ]]; then
                    echo "SKIP (exists): $result_file"
                    continue
                fi

                echo "RUN: $baseline | $dataset | ${pct}% | seed=$seed"
                "$PYTHON_EXEC" main_baseline.py \
                    -baseline "$baseline" \
                    -dataset "data/${dataset}.hf" \
                    -length "$length" \
                    -seed "$seed"
            done
        done
    done
done
echo "-----------------------------------"
echo "Simple baseline experiments processed"
echo "MELM starting"

for dataset in "${datasets[@]}"; do
    for pct in "${percentages[@]}"; do
        length=${lengths["${dataset}_${pct}"]}
        for seed in "${seeds[@]}"; do
            count=$((count + 1))

            result_file="./results/melm/${dataset}/${dataset}_${length}_${seed}.xlsx"

            echo -n "[$count/$total]"

            if [[ -f "$result_file" ]]; then
                echo "SKIP (exists): $result_file"
                continue
            fi

            echo "RUN: MELM | $dataset | ${pct}% | seed=$seed"
            "$PYTHON_EXEC" main_melm.py \
                -dataset "data/${dataset}.hf" \
                -length "$length" \
                -seed "$seed"
        done
    done
done

echo "-----------------------------------"
echo "MELM baseline experiments processed"
echo "Style_NER starting"

for dataset in "${datasets[@]}"; do
    for pct in "${percentages[@]}"; do
        length=${lengths["${dataset}_${pct}"]}
        for seed in "${seeds[@]}"; do
            count=$((count + 1))

            result_file="./results/style_NER/${dataset}/${dataset}_${length}_${seed}.xlsx"

            echo -n "[$count/$total]"

            if [[ -f "$result_file" ]]; then
                echo "SKIP (exists): $result_file"
                continue
            fi

            echo "RUN: style_NER | $dataset | ${pct}% | seed=$seed"
            "$PYTHON_EXEC" main_style_NER.py \
                -dataset "data/${dataset}.hf" \
                -length "$length" \
                -seed "$seed"
        done
    done
done

echo "-----------------------------------"
echo "All baseline experiments processed"