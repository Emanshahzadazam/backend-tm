from fastapi import APIRouter, HTTPException
from app.models.task import Task
from app.controllers import task_controller

router = APIRouter()

tasks = []

@router.get("/")
def home():
    return {"message": "Hello Backend Developer 🔥"}

@router.get("/tasks")
def get_tasks(completed: bool = None, search: str = None):
    return task_controller.get_all_tasks(tasks, completed, search)
@router.get("/tasks")
def get_tasks(completed: bool = None, search: str = None):
    return task_controller.get_all_tasks(tasks, completed, search)
@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    updated = task_controller.update_task(tasks, task_id, updated_task.model_dump())
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="task not found")
@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    updated = task_controller.update_task(tasks, task_id, updated_task.model_dump())
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="task not found")