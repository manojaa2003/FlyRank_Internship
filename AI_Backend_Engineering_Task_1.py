from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": True
    },
    {
        "id": 2,
        "title": "Build a simple API",
        "done": False
    },
    {
        "id": 3,
        "title": "Deploy the API",
        "done": False
    }
]
@app.get("/")
async def root():
    return {
        "name" : "Task API",
        "version": " 1.0",
        "endpoints" : ["/tasks"]
    }

@app.get("/health")
async def health():
    return {
        "status" : "ok"
    }

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return JSONResponse(
        status_code=404, 
        content={"error": f"Task {task_id} not found"}
        )