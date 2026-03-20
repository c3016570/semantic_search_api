def load_documents(path = "documents.txt"):

    with open(path, "r", encoding = "utf-8") as f:
        text = f.read()

    return text