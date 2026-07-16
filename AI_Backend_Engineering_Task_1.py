from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

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
    title : Optional[str] = Field(default=None,description="Title of the task to be created.")

class UpdateTask(BaseModel):
    title: Optional[str] = Field(default=None,description="Updated title of the task.")
    done: Optional[bool] = Field(default=None,description="Marks the task as completed (true) or pending (false).")

def get_data(id):
    for task in tasks:
        if task["id"] == id:
            return task

@app.get("/",summary="API Home",description="Returns basic information about the Task API, including its version and available endpoints.")
async def root():
    return {
        "name" : "Task API",
        "version": " 1.0",
        "endpoints" : ["/tasks"]
    }

@app.get("/health", summary="Health Check",description="Checks whether the Task API service is running and available.")
async def health():
    return {
        "status" : "ok"
    }

@app.get("/tasks",summary="Get All Tasks",description="Retrieves the complete list of tasks currently stored in memory.")
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}",summary="Get Task by ID",description="Retrieves a specific task using its unique task ID. Returns 404 if the task does not exist.")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return JSONResponse(
        status_code=404, 
        content={"error": f"Task {task_id} not found"}
    )

@app.post("/tasks", status_code=201,summary="Create Task",description="Creates a new task with the next available ID and sets its completion status to false.")
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

@app.put("/tasks/{task_id}",status_code=200,summary="Update Task",description="Updates the title and/or completion status of an existing task. Returns 404 if the task is not found.")
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

@app.delete("/tasks/{task_id}",status_code=204,summary="Delete Task",description="Deletes an existing task using its ID. Returns 404 if the task does not exist.")
async def delete_task(task_id: int):
    task = get_data(task_id)
    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"}
        )
    tasks.remove(task)
    return {"message": f"Task {task_id} deleted successfully"}