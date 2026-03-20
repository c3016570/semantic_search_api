import streamlit as st
import requests

st.title("Semantic Search Engine")

query1 = st.text_input("Enter your search")

if st.button("Search"):
    response = requests.post(
        "http://127.0.0.1:5000/search",
        json = {"query": query1}
    )

    if response.status_code == 200:
        results = response.json()["results"]
        for r in results:
            st.write(r)
    else:
        st.write(response.text)


query2 = st.text_input("Ask a question")

if st.button("Ask"):
    response = requests.post(
        "http://127.0.0.1:5000/chat",
        json = {"query": query2}
    )

    if response.status_code == 200:
        data = response.json()
        st.subheader("Answer")
        st.write(data["answer"])

        st.subheader("Retrieved Context")
        for doc in data["context"]:
            st.write("-", doc)

    else:
        st.write("Server error:")
        st.write(response.text)
