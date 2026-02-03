from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

def test_create_task():
    response = client.post(
        "/create/",
        json={
            "title": "Learn CI/CD",
            "description": "FastAPI pipeline test"
        }
    )
    assert response.status_code in [200, 201, 202]

def test_ci_is_working():
    # CI trigger check
    assert True