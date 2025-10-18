# Project Structure

```
interview-questions-project/
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI/CD
├── src/
│   ├── __init__.py
│   ├── helper.py                  # Core LLM pipeline functions
│   ├── prompt.py                  # Question generation prompts
│   └── config.py                  # Configuration management
├── templates/
│   └── index.html                 # Web interface template
├── static/
│   ├── docs/                     # Uploaded PDF files (gitignored)
│   │   └── README.md
│   └── output/                   # Generated CSV files (gitignored)
│       └── README.md
├── data/                         # Sample PDF files (gitignored)
│   └── README.md
├── .gitignore                    # Git ignore rules
├── env.example                   # Environment variables template
├── requirements.txt              # Python dependencies
├── setup.py                      # Package setup
├── install_dependencies.sh       # Installation script
├── start_web_app.sh             # Web app startup script
├── start_streamlit.sh           # Streamlit startup script
├── app.py                       # FastAPI web application
├── streamlit_app.py             # Streamlit application
├── README.md                    # Main documentation
├── CONTRIBUTING.md              # Contribution guidelines
├── LICENSE                      # MIT License
└── PROJECT_STRUCTURE.md         # This file
```

## Key Files

- **`src/helper.py`**: Core functionality for PDF processing and Q&A generation
- **`src/config.py`**: Configuration management and environment variables
- **`app.py`**: FastAPI web application with REST API endpoints
- **`streamlit_app.py`**: Streamlit interface for interactive use
- **`requirements.txt`**: All Python dependencies with versions

## Ignored Files

The following directories are ignored by Git for privacy and security:
- `venv/` - Virtual environment
- `static/docs/` - Uploaded PDF files
- `static/output/` - Generated CSV files
- `data/` - Sample PDF files
- `.env` - Environment variables with secrets
