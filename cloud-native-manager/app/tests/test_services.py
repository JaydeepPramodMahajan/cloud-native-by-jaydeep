from app.schemas.tasks import TaskCreate
from app.services.task_service import create_task, tasks


def test_create_tasks():
    tasks.clear()  # Each test should start with a clean environment.
    # Putting the default values to check
    # Inserting testing values
    task = TaskCreate(title="Develop project", description="On 24-6-2026")

    created_task = create_task(task)
    # Checking the results
    assert created_task.id == 1
    assert created_task.title == "Develop project"
    assert created_task.description == "On 24-6-2026"
    assert created_task.completed == False
    assert created_task.created_at is not None
