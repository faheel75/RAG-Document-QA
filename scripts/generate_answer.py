import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

model_name = 't5-small'
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

def generate_answer(question, context):
    input_text = f"question: {question} context: {context} "
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    outputs = model.generate(input_ids)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

