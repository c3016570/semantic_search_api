import faiss
import numpy as np

from model import encode_text
from data import documents
from data import chunks

doc_embeddings = encode_text(documents)
dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))


# Create embeddings for all the chunks
# chunk_embeddings = encode_text(chunks)

# Convert to numpy array
# chunk_embeddings = np.array(chunk_embeddings)

# Dimension of embeddings
# dimension = chunk_embeddings.shape[1]

# Create FAISS index
# index = faiss.IndexFlatL2(dimension)

# Add embeddings to index
# index.add(chunk_embeddings)


def search(query, top_k = 3):

    # encode query
    query_embedding = encode_text([query])[0]

    # convert to numpy and reshape for FAISS
    query_embedding = np.array(query_embedding).reshape(1,-1)

    # search FAISS index
    distances, indices = index.search(query_embedding, top_k)

    # retrieve relevant chunks
    results = [documents[i] for i in indices[0]]

    # similarities = np.dot(doc_embeddings, query_embedding)
    # top_indices = similarities.argsort()[-top_k:][::-1]

    
    # results = [documents[i] for i in top_indices]
    # results = [documents[i] for i in indices[0]]
    return results, distances[0]