# **Chatbot Document Retriever 🤖📚**

Welcome to the **Chatbot Document Retriever**! This project uses **LangChain**, **OpenAI**, and **Chroma** to create a smart, document-retrieving AI chatbot. It lets you upload a folder full of **Markdown documents** and interact with a **GPT-4 powered model** to retrieve relevant info, all through a sleek Gradio interface. 🚀

### **✨ Features**

-   **Intelligent Document Processing**: Automatically loads and processes **Markdown files** from a local folder.
-   **Efficient Chunking**: Splits large documents into digestible chunks for quick and accurate retrieval.
-   **Embeddings for Speed**: Uses **Chroma** to store document embeddings for fast and scalable querying.
-   **Interactive Chatbot**: Ask questions based on your documents, and get smart answers powered by **GPT-4**.
-   **Gradio Interface**: Easy-to-use web interface to chat with your AI bot and get real-time responses. 💬

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/capi20/Chatbot-Doc-RAG.git
cd Chatbot-Doc-RAG
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenAI API Key

Create a .env file in the root of the project:

```bash
# .env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Usage

Run the app with:

```bash
python main.py
```

This will launch a Gradio web interface in your browser automatically.

---
