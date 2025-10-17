#!/bin/bash

# PDF Interview Question Generator - Dependency Installation Script

echo "📦 Installing PDF Interview Question Generator Dependencies..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "🐍 Python version: $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing Python dependencies..."
pip install -r requirements.txt

# Check if Ollama is installed
echo "🔍 Checking Ollama installation..."
if command -v ollama &> /dev/null; then
    echo "✅ Ollama is installed"
    
    # Check if Ollama is running
    if curl -s http://localhost:11434/api/tags > /dev/null; then
        echo "✅ Ollama is running"
        
        # Check if llama3 model is installed
        if ollama list | grep -q "llama3"; then
            echo "✅ llama3 model is installed"
        else
            echo "⚠️  llama3 model not found. Installing..."
            ollama pull llama3
        fi
    else
        echo "⚠️  Ollama is not running. Please start it with: ollama serve"
    fi
else
    echo "⚠️  Ollama is not installed. Please install it from: https://ollama.ai/"
    echo "   After installation, run: ollama pull llama3"
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "To start the applications:"
echo "  Web App:     ./start_web_app.sh"
echo "  Streamlit:   ./start_streamlit.sh"
echo ""
echo "Make sure to set your Google API key in the .env file (optional):"
echo "  GOOGLE_API_KEY=your_api_key_here"
