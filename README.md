# 📄 LLM Interview Question&Answer Generator

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-FE1A42.svg)](https://www.langchain.com/)
[![Ollama](https://img.shields.io/badge/Local%20LLM-Ollama%20%7C%20Llama3-000000.svg)](https://ollama.com/)
[![FAISS](https://img.shields.io/badge/Vector%20Store-FAISS-red.svg)](https://github.com/facebookresearch/faiss)
[![Google GenAI](https://img.shields.io/badge/Embeddings-Google%20GenAI-4285F4.svg)](https://ai.google.dev/)
[![PDF Processing](https://img.shields.io/badge/PDF%20Processing-PyPDF-FF0000.svg)](https://pypdf.readthedocs.io/en/stable/)

A powerful AI-powered application that generates interview questions and answers from PDF documents. Available in both web interface (FastAPI) and Streamlit versions.

## ✨ Features

- **PDF Processing**: Extract text from PDF documents
- **AI-Powered Q&A Generation**: Uses Ollama with llama3 model for intelligent question and answer generation
- **Multiple Interfaces**: Choose between web app or Streamlit interface
- **Flexible Embeddings**: Supports both Google Generative AI and HuggingFace embeddings
- **CSV Export**: Download generated questions and answers as CSV files
- **Error Handling**: Robust error handling and user feedback

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running
- llama3 model installed in Ollama

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/interview-questions-project.git
   cd interview-questions-project
   ```

2. **Run the installation script**:
   ```bash
   chmod +x *.sh
   ./install_dependencies.sh
   ```

3. **Start Ollama** (if not running):
   ```bash
   ollama serve
   ollama pull llama3
   ```

### Running the Applications

#### Option 1: Web Application (FastAPI)
```bash
./start_web_app.sh
```
- Access at: http://localhost:8080
- API docs at: http://localhost:8080/docs

#### Option 2: Streamlit Application
```bash
./start_streamlit.sh
```
- Access at: http://localhost:8501

## 🔧 Configuration

### Environment Variables (Optional)

Create a `.env` file in the project root:

```env
# Google Generative AI API Key (optional - for better embeddings)
GOOGLE_API_KEY=your_google_api_key_here

# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3

# Application Settings
MAX_PAGES=5
CHUNK_SIZE=10000
CHUNK_OVERLAP=200
```

### Ollama Setup

1. **Install Ollama**: Visit [ollama.ai](https://ollama.ai/)
2. **Start Ollama service**:
   ```bash
   ollama serve
   ```
3. **Install llama3 model**:
   ```bash
   ollama pull llama3
   ```

## 📁 Project Structure

```
interview-questions-project/
├── src/
│   ├── helper.py          # Core LLM pipeline functions
│   ├── prompt.py          # Question generation prompts
│   └── config.py          # Configuration management
├── templates/
│   └── index.html         # Web interface template
├── static/
│   ├── docs/              # Uploaded PDF files
│   └── output/            # Generated CSV files
├── app.py                 # FastAPI web application
├── streamlit_app.py       # Streamlit application
├── requirements.txt       # Python dependencies
├── install_dependencies.sh # Installation script
├── start_web_app.sh       # Web app startup script
├── start_streamlit.sh     # Streamlit startup script
└── README.md              # This file
```

## 🎯 Usage

### Web Application

1. Open http://localhost:8080
2. Upload a PDF file (max 10MB)
3. Click "Generate Q&A"
4. Download the generated CSV file

### Streamlit Application

1. Open http://localhost:8501
2. Configure Ollama settings in the sidebar
3. Upload a PDF file
4. Click "Generate Questions & Answers"
5. View results and download CSV

## 🔍 How It Works

1. **PDF Processing**: Extracts text from uploaded PDF files
2. **Text Chunking**: Splits content into manageable chunks
3. **Question Generation**: Uses AI to generate relevant interview questions
4. **Answer Generation**: Creates comprehensive answers using RAG (Retrieval Augmented Generation)
5. **Export**: Saves results as CSV for easy use

## 🛠️ Technical Details

### Dependencies

- **LangChain**: Framework for LLM applications
- **Ollama**: Local LLM inference
- **FastAPI**: Web framework
- **Streamlit**: Data app framework
- **FAISS**: Vector similarity search
- **PyPDF**: PDF text extraction

### Models Used

- **LLM**: llama3 (via Ollama)
- **Embeddings**: Google Generative AI or HuggingFace (fallback)

## 🐛 Troubleshooting

### Common Issues

1. **Ollama not running**:
   ```bash
   ollama serve
   ```

2. **llama3 model not found**:
   ```bash
   ollama pull llama3
   ```

3. **Port already in use**:
   - Web app: Change port in `start_web_app.sh`
   - Streamlit: Change port in `start_streamlit.sh`

4. **Memory issues**:
   - Reduce `CHUNK_SIZE` in config
   - Use smaller PDF files

5. **NumPy compatibility warnings**:
   - These warnings are harmless and don't affect functionality
   - The application will work correctly despite the warnings

6. **Architecture compatibility issues**:
   - Always use the virtual environment: `source venv/bin/activate`
   - If you encounter import errors, reinstall dependencies in the venv

### Error Messages

- **"Ollama is not running"**: Start Ollama service
- **"Model not found"**: Install llama3 model
- **"PDF file not found"**: Check file path and permissions
- **"No content found"**: Ensure PDF contains extractable text

## 📝 API Endpoints (Web App)

- `GET /`: Main web interface
- `POST /upload`: Upload PDF file
- `POST /analyze`: Generate questions and answers
- `GET /download/{filename}`: Download generated CSV
- `GET /docs`: API documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Author information redacted
 - Email: redacted

## 🙏 Acknowledgments

- Ollama team for the excellent local LLM platform
- LangChain team for the comprehensive LLM framework
- FastAPI and Streamlit teams for the web frameworks
