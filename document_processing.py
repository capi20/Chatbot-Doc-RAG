# document_processing.py
from langchain.text_splitter import CharacterTextSplitter

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    """Split the loaded documents into smaller chunks."""
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(documents)
    return chunks
