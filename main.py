from fastapi import FastAPI, Form
from jobs.pipeline import process_video

from db.sessions import Base, engine
from db.crud import get_task

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/process-youtube")
def process(youtube_url: str = Form(...)):
    print(f"initial youtube_url:{youtube_url}")
    task_id = process_video(youtube_url)
    return {"status": "processing", "task_id": task_id}


@app.get("/status/{task_id}")
def check_status(task_id: str):
    task = get_task(task_id)
    if task:
        return {"task_id": task.id, "status": task.status}
    return {"error": "Task not found"}, 404
