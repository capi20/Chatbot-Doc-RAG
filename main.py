import glob
from env_setup import setup_environment
from document_loader import load_documents
from document_processing import split_documents
from vector_store import setup_vector_store
from model_setup import setup_model_and_memory
from chat_interface import chat, launch_chat_interface
from langchain_openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain

# Initialize environment
setup_environment()

# Define constants
MODEL = "gpt-4o-mini"
db_name = "vector_db"
folders = glob.glob("knowledge_base/*")
text_loader_kwargs = {'encoding': 'utf-8'}

# Load documents
documents = load_documents(folders, text_loader_kwargs)

# Process documents by splitting into smaller chunks
chunks = split_documents(documents)

# Set up embeddings for vector store
embeddings = OpenAIEmbeddings()

# Set up the vector store
vectorstore = setup_vector_store(chunks, db_name, embeddings)

# Initialize the language model and memory
llm, memory = setup_model_and_memory(MODEL)

# Set up retriever to retrieve documents from the vector store
retriever = vectorstore.as_retriever(search_kwargs={"k": 25})

# Create the conversation chain
conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)

# Launch the chat interface
launch_chat_interface(lambda question, history: chat(question, history, conversation_chain))
