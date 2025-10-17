import streamlit as st
import os
import tempfile
import pandas as pd
import csv
import io
from src.helper import llm_pipeline
from src.config import *

# Page configuration
st.set_page_config(
    page_title="PDF Interview Question Generator",
    page_icon="📄",
    layout="wide"
)

st.title("📄 PDF Interview Question Generator")
st.markdown("Upload your PDF file and generate interview questions and answers automatically.")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    st.info("Make sure Ollama is running with the llama3 model")
    
    # Model settings
    ollama_url = st.text_input("Ollama URL", value=OLLAMA_BASE_URL)
    model_name = st.text_input("Model Name", value=OLLAMA_MODEL)
    
    # API Key settings
    google_api_key = st.text_input("Google API Key (Optional)", value=GOOGLE_API_KEY, type="password")
    if google_api_key:
        st.success("Google API Key provided - will use Google embeddings")
    else:
        st.info("No Google API Key - will use HuggingFace embeddings")

# Main content
uploaded_file = st.file_uploader("Upload your PDF file", type="pdf", help="Maximum recommended: 5 pages")

if uploaded_file is not None:
    # Display file info
    st.success(f"File uploaded: {uploaded_file.name}")
    st.info(f"File size: {uploaded_file.size} bytes")
    
    if st.button("🚀 Generate Questions & Answers", type="primary"):
        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name
            
            # Show progress
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("📄 Processing PDF...")
            progress_bar.progress(20)
            
            # Update config with user inputs
            import src.config as config
            config.OLLAMA_BASE_URL = ollama_url
            config.OLLAMA_MODEL = model_name
            config.GOOGLE_API_KEY = google_api_key
            
            status_text.text("🤖 Generating questions...")
            progress_bar.progress(40)
            
            # Run the LLM pipeline
            answer_generation_chain, ques_list = llm_pipeline(tmp_file_path)
            
            status_text.text("💭 Generating answers...")
            progress_bar.progress(60)
            
            # Generate answers for each question
            qa_data = []
            for i, question in enumerate(ques_list):
                if question.strip():
                    try:
                        answer = answer_generation_chain.invoke({"query": question})
                        qa_data.append({
                            "Question": question,
                            "Answer": answer["result"]
                        })
                        progress_bar.progress(60 + (i + 1) * 30 // len(ques_list))
                    except Exception as e:
                        st.warning(f"Error generating answer for question: {question}")
                        qa_data.append({
                            "Question": question,
                            "Answer": f"Error: {str(e)}"
                        })
            
            progress_bar.progress(100)
            status_text.text("✅ Complete!")
            
            # Display results
            st.success(f"Generated {len(qa_data)} questions and answers!")
            
            # Create DataFrame
            df = pd.DataFrame(qa_data)
            
            # Display the results
            st.subheader("📋 Generated Questions & Answers")
            st.dataframe(df, use_container_width=True)
            
            # Download functionality
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False, encoding='utf-8')
            csv_data = csv_buffer.getvalue()
            
            st.download_button(
                label="📥 Download Q&A as CSV",
                data=csv_data,
                file_name=f"QA_{uploaded_file.name.replace('.pdf', '')}.csv",
                mime="text/csv"
            )
            
            # Clean up temporary file
            os.unlink(tmp_file_path)
            
        except Exception as e:
            st.error(f"❌ Error processing PDF: {str(e)}")
            st.info("Please check that:")
            st.info("1. Ollama is running")
            st.info("2. The llama3 model is installed")
            st.info("3. Your PDF file is valid and not corrupted")
            
            # Clean up temporary file if it exists
            if 'tmp_file_path' in locals():
                try:
                    os.unlink(tmp_file_path)
                except:
                    pass

# Footer
st.markdown("---")
st.markdown("**Note:** This application uses Ollama with the llama3 model for question and answer generation.")