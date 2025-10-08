# chat_interface.py
import gradio as gr

def chat(question, history, conversation_chain):
    """Process the user's question through the conversation chain."""
    result = conversation_chain.invoke({"question": question})
    return result["answer"]

def launch_chat_interface(chat_function):
    """Launch the Gradio chat interface."""
    view = gr.ChatInterface(chat_function, type="messages").launch(inbrowser=True)
