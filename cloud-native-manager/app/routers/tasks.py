from app.schemas.tasks import Task, TaskCreate, Task_Updated
from fastapi import status, APIRouter
from app.services.task_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# Means By using router automaticallly we will get the /task insteadof manually typing it
#
@router.post( "/",response_model=Task,#Describing that the Final Value is Task Schema 
             status_code=status.HTTP_201_CREATED,  # Another way to wite status_code=201
)
async def add_task(task: TaskCreate):
    return create_task(task)


@router.get("/", response_model=list[Task])
def get_router_tasks():
    return get_all_tasks()


@router.get("/{task_id}", response_model=Task)
def search_task_by_id(task_id: int):
    return get_task_by_id(task_id)


@router.put("/{task_id}", response_model=Task)
def update_the_data(task_id: int, task: Task_Updated):
    return update_task(task_id, task)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_by_id(task_id: int):
    return delete_task(task_id)
