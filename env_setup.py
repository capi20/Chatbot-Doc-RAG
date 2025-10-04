# env_setup.py
import os
from dotenv import load_dotenv

def setup_environment():
    """Load environment variables and set OpenAI API key."""
    load_dotenv(override=True)
    
    # Check that the key is loaded
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
