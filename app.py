from fastapi import FastAPI, Request, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import aiofiles
import uuid 
import csv
from src.helper import llm_pipeline, file_preprocessing
from src.config import *


app = FastAPI(
    title="LLM Question Answer Generator",
    description="Generate interview questions and answers from PDF documents",
    version="1.0.0"
)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Ensure directories exist
os.makedirs("static/docs", exist_ok=True)
os.makedirs("static/output", exist_ok=True)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    """
    PDF dosyasını yükler ve kaydeder. Boyut veya sayfa sınırı kontrolü yoktur.
    """
    try:
        
        if not pdf_file.filename.lower().endswith('.pdf'):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed")

        unique_filename = f"{uuid.uuid4()}_{pdf_file.filename.replace(' ', '_')}"
        pdf_path = os.path.join("static/docs", unique_filename)

        content = await pdf_file.read()

        async with aiofiles.open(pdf_path, 'wb') as f:
            await f.write(content)

        return JSONResponse(content={"msg": "success", "pdf_filename": pdf_path})
    
    except Exception as e:
        
        raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")

@app.post("/analyze")
async def analyze_pdf(pdf_filename: str = Form(...)):
    try:
     
        if not os.path.exists(pdf_filename):
            raise HTTPException(status_code=404, detail="PDF file not found")
        
        
        answer_generation_chain, ques_list = llm_pipeline(pdf_filename)
        
        output_filename = f"QA_{uuid.uuid4().hex[:8]}.csv"
        output_file = os.path.join("static/output", output_filename)
        
        with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Question", "Answer"])

            for question in ques_list:
                if question.strip():  
                    try:
                        answer = answer_generation_chain.invoke({"query": question})
                        csv_writer.writerow([question, answer["result"]])
                    except Exception as e:
                        csv_writer.writerow([question, f"Error generating answer: {str(e)}"])
        
        return JSONResponse(content={
            "output_file": output_file,
            "questions_count": len(ques_list),
            "message": "Questions and answers generated successfully"
        })
    
    except Exception as e:
    
        raise HTTPException(status_code=500, detail=f"Error analyzing PDF: {str(e)}")

@app.get("/download/{filename}")
async def download_file(filename: str):
    """Download generated CSV files"""
    file_path = os.path.join("static/output", filename)
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path,
            filename=filename,
            media_type="text/csv"
        )
    else:
        raise HTTPException(status_code=404, detail="File not found")

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=8080, reload=True)