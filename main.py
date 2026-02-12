from fastapi import FastAPI, UploadFile, File
import shutil

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/api/recognize")
async def recognize(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"status": "file received"}
