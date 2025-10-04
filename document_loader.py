# document_loader.py
import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

def load_documents(folders, text_loader_kwargs):
    """Load documents from the specified folders and add metadata."""
    documents = []
    for folder in folders:
        doc_type = os.path.basename(folder)
        loader = DirectoryLoader(folder, glob="**/*.pdf", loader_cls=PyPDFLoader)
        folder_docs = loader.load()
        documents.extend([add_metadata(doc, doc_type) for doc in folder_docs])
    return documents

def add_metadata(doc, doc_type):
    """Add metadata to the document (e.g., doc type)."""
    doc.metadata["doc_type"] = doc_type
    return doc
