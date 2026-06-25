from datetime import datetime
from app.schemas.tasks import Task, TaskCreate, Task_Updated

tasks = []


def create_task(task: TaskCreate):
    new_task = Task(
        id=len(tasks) + 1,
        title=task.title,
        description=task.description,
        completed=False,
        created_at=datetime.now(),
    )
    tasks.append(new_task)
    return new_task


def get_all_tasks():
    return tasks


def get_task_by_id(tid: int):
    for i in tasks:
        if i.id == tid:
            return i
    return "Error Not Found"


def update_task(task_id: int, updated_task: Task_Updated):
    for i in tasks:
        if i.id == task_id:
            i.title = updated_task.title
            i.description = updated_task.description
            i.completed = updated_task.completed
            return i
        else:
            print("Error While Updating")
            return


def delete_task(task_id: int):
    for i in tasks:
        if i.id == task_id:
            tasks.remove(i)
            return
