import os
import json

def preprocess_documents(data_dir='data/raw', output_dir='data/processed'):
    os.makedirs(output_dir, exist_ok=True)
    docs = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(data_dir, filename), 'r') as file:
                text = file.read()
                chunks = [text[i:i+300] for i in range(0, len(text), 300)]
                docs.extend(chunks)
    with open(os.path.join(output_dir, 'processed_docs.json'), 'w') as f:
        json.dump(docs, f)

if __name__ == '__main__':
    preprocess_documents()

