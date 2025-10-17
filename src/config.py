import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Google Generative AI Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# Ollama Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

# Application Settings
MAX_PAGES = int(os.getenv("MAX_PAGES", "5"))
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "10000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))

# Model Settings
QUESTION_TEMPERATURE = 0.3
ANSWER_TEMPERATURE = 0.1
