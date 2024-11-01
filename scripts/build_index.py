import json
import faiss
from sentence_transformers import SentenceTransformer

def build_faiss_index(data_file='data/processed/processed_docs.json', model_name='sentence-transformers/all-MiniLM-L6-v2'):
    with open(data_file, 'r') as f:
        docs = json.load(f)

    model = SentenceTransformer(model_name)
    embeddings = model.encode(docs)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, 'models/faiss_index')
    with open('models/documents.json', 'w') as f:
        json.dump(docs, f)

if __name__ == '__main__':
    build_faiss_index()

