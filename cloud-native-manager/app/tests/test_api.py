from fastapi.testclient import TestClient  # Allows to send Fake HTTP request

from app.main import app
from app.services.task_service import tasks

client = TestClient(app)  # Behaving like Automated Postman


def test_create_post_api():
    tasks.clear()


# Feeding the Testing data
response = client.post(
    "/tasks/", json={"title": "Api testing Demo", "description": "On 26-04-2026"}
)
# Checking that Feeded is same or not
data = response.json()
assert response.status_code == 201
assert data["title"] == "Api testing Demo"
assert data["description"] == "On 26-04-2026"
assert data["completed"] is False


def test_create_get_api():
    tasks.clear()
    client.post("/tasks/", json={"title": "Task 1", "description": "On 24-06-2026"})


response = client.get("/tasks/")
assert response.status_code == 200

data = response.json()
assert len(data) == 1
assert data[0]["title"] == "Task 1"


def test_get_by_id():
    tasks.clear()
    client.post("/tasks/", json={"title": "Testing By id", "description": "By_id"})
    response = client.get("/task/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Testing By id"
