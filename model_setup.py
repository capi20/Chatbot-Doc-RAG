# model_setup.py
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

def setup_model_and_memory(model_name, temperature=0.7):
    """Set up the language model and memory for the conversation chain."""
    # Initialize the language model with specific settings
    llm = ChatOpenAI(temperature=temperature, model_name=model_name)
    
    # Set up memory to store the chat history
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    
    return llm, memory
