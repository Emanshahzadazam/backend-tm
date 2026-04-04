from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Backend Developer 🔥 "}

class task(BaseModel):
    title:str
    completed:bool

tasks:list[task] = []

@app.get("/tasks")
def viewtask():
    return tasks

@app.post("/tasks", status_code=201)
def addtasks(task:task):
    tasks.append(task.model_dump())
    return {"message": "task added successfully", "task":task}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: task):
    if 1<= task_id < len(tasks):
        tasks[task_id-1] = updated_task
        return {"message": "task updated successfully", "task": updated_task}
    raise HTTPException(status_code=404, detail="task not found")

@app.delete("/tasks/{task_id}")
def deletetask(tasks_id: int):
    if 1<=tasks_id<=len(tasks):
        deltask=tasks.pop(tasks_id-1)
        return {"message": "task deleted successfully", "task": deltask}
    raise HTTPException(status_code=404, detail="task not found")
   
