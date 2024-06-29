#!/bin/bash
python ie2instruction/convert_func.py \
    --src_path ./sample.json \
    --tgt_path ./KG_test.json \
    --schema_path ./KG_schema.json \
    --language zh \
    --task KG \
    --split_num 1 \
    --split test

CUDA_VISIBLE_DEVICES=0 python src/inference.py \
    --stage sft \
    --model_name_or_path '../../../../OneKE' \
    --model_name 'llama' \
    --template 'llama2_zh' \
    --do_predict \
    --input_file './KG_test.json' \
    --output_file './KG_output.json' \
    --output_dir './test' \
    --predict_with_generate \
    --cutoff_len 512 \
    --fp16 \
    --max_new_tokens 300 \
    --bits 4

python ie2instruction/convert_func.py \
    --src_path ./sample.json \
    --tgt_path ./SPO_test.json \
    --schema_path ./SPO_schema.json \
    --language zh \
    --task SPO \
    --split_num 4 \
    --split test

CUDA_VISIBLE_DEVICES=0 python src/inference.py \
    --stage sft \
    --model_name_or_path '../../../../OneKE' \
    --model_name 'llama' \
    --template 'llama2_zh' \
    --do_predict \
    --input_file './SPO_test.json' \
    --output_file './SPO_output.json' \
    --output_dir './test' \
    --predict_with_generate \
    --cutoff_len 512 \
    --fp16 \
    --max_new_tokens 300 \
    --bits 4
