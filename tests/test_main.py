from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message":"Fastapi"}

def test_home():
    response = client.get("/home")

    assert response.status_code == 200
    assert response.json() == {"message":"Welcome to home"}