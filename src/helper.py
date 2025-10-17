from langchain_community.document_loaders import PyPDFLoader 
from langchain_core.documents import Document 
from langchain.text_splitter import TokenTextSplitter, RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate 
from langchain.chains.summarize import load_summarize_chain
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from src.prompt import * 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.config import *
import os

def file_preprocessing(file_path): 
    """
    Preprocess PDF file and split into chunks for question and answer generation.
    
    Args:
        file_path (str): Path to the PDF file
        
    Returns:
        tuple: (document_ques_gen, document_answer_gen) - Lists of Document objects
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF file not found: {file_path}")
    
    # Load the data from PDF 
    loader = PyPDFLoader(file_path)
    data = loader.load() 
    
    if not data:
        raise ValueError("No content found in the PDF file")

    question_gen = '' 

    for page in data:
        question_gen += page.page_content 

    # Use RecursiveCharacterTextSplitter for better compatibility
    splitter_ques_gen = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunk_ques_gen = splitter_ques_gen.split_text(question_gen)

    document_ques_gen = [Document(page_content=t) for t in chunk_ques_gen]

    splitter_ans_gen = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP//2,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    # Convert text chunks to Document objects
    answer_chunks = splitter_ans_gen.split_text(question_gen)
    document_answer_gen = [Document(page_content=chunk) for chunk in answer_chunks] 

    return document_ques_gen, document_answer_gen 


def llm_pipeline(file_path): 
    """
    Main LLM pipeline for generating questions and answers from PDF.
    
    Args:
        file_path (str): Path to the PDF file
        
    Returns:
        tuple: (answer_generation_chain, filtered_ques_list) - Chain for answering and list of questions
    """
    try:
        document_ques_gen, document_answer_gen = file_preprocessing(file_path) 

        # Initialize Ollama LLM for question generation
        llm_ques_gen_pipeline = OllamaLLM(
            model=OLLAMA_MODEL, 
            temperature=QUESTION_TEMPERATURE,
            base_url=OLLAMA_BASE_URL
        )

        PROMPT_QUESTION = PromptTemplate(template=prompt_template, input_variables=["text"]) 

        REFINE_PROMPT_QUESTIONS = PromptTemplate( 
            input_variables=["existing_answer", "text"], 
            template=refine_template,
        )

        ques_gen_chain = load_summarize_chain(
            llm=llm_ques_gen_pipeline,
            chain_type="refine",
            verbose=True,
            question_prompt=PROMPT_QUESTION,
            refine_prompt=REFINE_PROMPT_QUESTIONS
        )
        
        ques = ques_gen_chain.run(document_answer_gen) 

        # Initialize embeddings - use Google Generative AI if API key is available, otherwise use HuggingFace
        if GOOGLE_API_KEY:
            embeddings = GoogleGenerativeAIEmbeddings(
                model="models/embedding-001",
                google_api_key=GOOGLE_API_KEY
            )
        else:
            from langchain_huggingface import HuggingFaceEmbeddings
            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )

        vector_store = FAISS.from_documents(document_answer_gen, embeddings)

        # Initialize Ollama LLM for answer generation
        llm_answer_gen = OllamaLLM(
            model=OLLAMA_MODEL, 
            temperature=ANSWER_TEMPERATURE,
            base_url=OLLAMA_BASE_URL
        ) 

        ques_list = ques.split("\n") 
        filtered_ques_list = [element.strip() for element in ques_list 
                             if element.strip() and (element.strip().endswith('?') or element.strip().endswith('.'))] 

        answer_generation_chain = RetrievalQA.from_chain_type(
            llm=llm_answer_gen, 
            chain_type="stuff", 
            retriever=vector_store.as_retriever()
        )

        return answer_generation_chain, filtered_ques_list
        
    except Exception as e:
        raise Exception(f"Error in LLM pipeline: {str(e)}") 