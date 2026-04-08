from fastapi import APIRouter, HTTPException
from app.models.task import Task

router = APIRouter()

tasks = []

@router.get("/")
def home():
    return {"message": "Hello Backend Developer 🔥"}

@router.get("/tasks")
def get_tasks(completed: bool = None, search: str = None):
    result = tasks

    if completed is not None:
        result = [task for task in result if task["completed"] == completed]

    if search is not None:
        result = [
            task for task in result
            if search.lower() in task["title"].lower()
        ]

    return result

@router.post("/tasks", status_code=201)
def add_task(task: Task):
    task_dict = task.model_dump()
    tasks.append(task_dict)
    return {"message": "task added successfully", "task": task_dict}

@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1] = updated_task.model_dump()
        return {"message": "task updated successfully", "task": tasks[task_id - 1]}
    raise HTTPException(status_code=404, detail="task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if 1 <= task_id <= len(tasks):
        deleted = tasks.pop(task_id - 1)
        return {"message": "task deleted successfully", "task": deleted}
    raise HTTPException(status_code=404, detail="task not found")