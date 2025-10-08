# vector_store.py
import os
from langchain_chroma import Chroma

def setup_vector_store(documents, db_name, embeddings):
    """Create and store documents in a vector database."""
    # Check if the database exists, delete it if so
    if os.path.exists(db_name):
        Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()

    # Create a new vector store with the given documents and embeddings
    vectorstore = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=db_name)
    return vectorstore
