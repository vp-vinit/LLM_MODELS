
from fastapi import FastAPI, UploadFile, File, Form

app = FastAPI()

@app.post("/ask")
def ask_pdf(
    file: UploadFile = File(...),
    question: str = Form(...)
):
    return {
        "Filename": file.filename,
        "question": question
    }


