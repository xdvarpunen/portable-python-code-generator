import os
import re
import argparse
from tqdm import tqdm

from transformers import pipeline, set_seed
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers.pipelines.base import Pipeline


def load_generation_pipe(model_name_or_path: str, gpu_device: int=0):
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path)
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)


    pipe = pipeline(
        'text-generation',
        model=model,
        tokenizer=tokenizer,
        device="cpu" # Have no CUDA installed https://discuss.huggingface.co/t/is-transformers-using-gpu-by-default/8500
    )

    print("load generation pipeline from {} over, vocab size = {}, eos id = {}, gpu device = {}.".format(
        model_name_or_path, len(tokenizer), tokenizer.eos_token_id, gpu_device)
    )

    return pipe

def extract_function_block(string):
    return re.split("\nclass|\ndef|\n#|\n@|\nprint|\nif", string)[0].rstrip()

def run_code_generation(pipe, prompt, num_completions=1, **gen_kwargs):
    set_seed(123)

    code_gens = pipe(prompt,
        num_return_sequences=num_completions,
        **gen_kwargs
    )

    return [extract_function_block(code_gen["generated_text"][len(prompt):]) for code_gen in code_gens]

pipe = load_generation_pipe("Daoguang/PyCodeGPT", 0)

gen_kwargs = {
    "do_sample": True,
    "temperature": 0.8,
    "max_new_tokens": 150,
    "top_p": 0.9,
    "top_k": 0,
    "pad_token_id": pipe.tokenizer.pad_token_id if pipe.tokenizer.pad_token_id else pipe.tokenizer.eos_token_id,
    "eos_token_id": pipe.tokenizer.eos_token_id
}

while True:
    print("Example: 'def say_hello():'")
    print("Example: How to draw rectangle in PyGame?")
    print("Press Ctrl+C to quit app.")
    prompt = input("Write prompt: ")
    code_gens = run_code_generation(pipe, prompt, num_completions=5, **gen_kwargs)
    [print(code_gen) for code_gen in code_gens]