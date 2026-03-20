from flask import Flask, request, jsonify
import numpy as np

from search import search, index
from data import documents
from model import encode_text

from generator import generate_answer


app = Flask(__name__)

@app.route("/")
def home():
    return "Semantic Search API"

@app.route("/search", methods = ["POST"])
def semantic_search():
    # below code is calling the dictionary returned in json
    # as a function : dict() which is incorrect

    # data = request.json()
    # correct alternative : data = request.get_json()
    # or as shown below
    data = request.json
    query = data["query"]

    results = search(query)

    return jsonify({
        "query": query,
        "results": results
    })

@app.route("/add_document", methods = ["POST"])
def add_document():
    data = request.json
    text = data["text"]

    documents.append(text)

    embedding = encode_text([text])
    index.add(np.array(embedding))

    return jsonify({"message":"document added"})


@app.route("/chat", methods = ["POST"])
def chat():
    data = request.json
    query = data["query"]

    context_docs, distances = search(query)

    if distances[0] > 1.2:
        return jsonify({
            "answer" : answer,
            "context" : context_docs
        })
    context = " ".join(context_docs)
    answer = generate_answer(query, context)
    return jsonify({
        "answer" : answer,
        "context" : context_docs
    })

if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)