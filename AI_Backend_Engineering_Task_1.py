from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

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

class CreateTask(BaseModel):
    title : Optional[str] = None

class UpdateTask(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

def get_data(id):
    for task in tasks:
        if task["id"] == id:
            return task

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

@app.post("/tasks", status_code=201)
async def create_task(task: CreateTask):
    if task.title is None or not task.title.strip():
        return JSONResponse(
            status_code=400,
            content={"error": "Title is required"}
        )
    next_id = 0
    for t in tasks:
        if t["id"] > next_id:
            next_id = t["id"]
    next_id += 1
    new_task = {
        "id": next_id,
        "title": task.title,
        "done": False
    }
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}",status_code=200)
async def update_task_data(task_id: int, update_task: UpdateTask):
    old_task = get_data(task_id)
    if old_task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"}
        )
    if update_task.title is not None:
        old_task["title"] = update_task.title
    if update_task.done is not None:
        old_task["done"] = update_task.done

    return old_task

@app.delete("/tasks/{task_id}",status_code=204)
async def delete_task(task_id: int):
    task = get_data(task_id)
    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"}
        )
    tasks.remove(task)
    return {"message": f"Task {task_id} deleted successfully"}