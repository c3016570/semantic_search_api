from transformers import pipeline
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

def encode_text(texts):
    return model.encode(texts)

generator = pipeline(
    "text-generation",
    model = "google/flan-t5-base"
)