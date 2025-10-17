#!/bin/bash

# PDF Interview Question Generator - Streamlit App Startup Script

echo "🚀 Starting PDF Interview Question Generator Streamlit Application..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if virtual environment exists, if not create one
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Check if Ollama is running
echo "🔍 Checking Ollama status..."
if ! curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "⚠️  Warning: Ollama is not running on localhost:11434"
    echo "   Please start Ollama and ensure the llama3 model is installed:"
    echo "   ollama pull llama3"
    echo ""
fi

# Start the Streamlit application
echo "📊 Starting Streamlit application..."
echo "   Streamlit interface will be available at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
