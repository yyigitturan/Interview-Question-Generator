# Contributing to PDF Interview Question Generator

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the PDF Interview Question Generator.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a virtual environment
4. Install dependencies
5. Make your changes
6. Test your changes
7. Submit a pull request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/interview-questions-project.git
cd interview-questions-project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Ollama and llama3 model
ollama pull llama3
```

## Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small

## Testing

Before submitting a pull request, please:

1. Test both Streamlit and FastAPI applications
2. Test with different PDF files
3. Ensure error handling works correctly
4. Check that all dependencies are properly listed

## Pull Request Process

1. Create a feature branch from `main`
2. Make your changes
3. Test thoroughly
4. Update documentation if needed
5. Submit a pull request with a clear description

## Issues

When reporting issues, please include:

- Operating system and Python version
- Steps to reproduce the issue
- Expected vs actual behavior
- Any error messages

## Questions?

Feel free to open an issue for questions or discussions.
