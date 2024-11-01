import faiss
import json
from sentence_transformers import SentenceTransformer
from generate_answer import generate_answer

def load_index(index_file='models/faiss_index', docs_file='models/documents.json'):
    index = faiss.read_index(index_file)
    with open(docs_file, 'r') as f:
        docs = json.load(f)
    return index, docs

def retrieve(query, index, docs, model_name='sentence-transformers/all-MiniLM-L6-v2', k=5):
    model = SentenceTransformer(model_name)
    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, k)
    return [docs[idx] for idx in indices[0]]

def answer_question(query):
    index, docs = load_index()
    retrieved_docs = retrieve(query, index, docs)
    context = " ".join(retrieved_docs)
    answer = generate_answer(query, context)
    return answer

