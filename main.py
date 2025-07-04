from fastapi import FastAPI, Form
from jobs.pipeline import process_video

app = FastAPI()

@app.post("/process-youtube")
def process(youtube_url: str = Form(...)):
    task_id = process_video(youtube_url)
    return {"status": "processing", "task_id": task_id}
