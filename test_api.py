from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_chat():
    response = client.post("/api/chat", json={"message": "Hello"})
    assert response.status_code == 200
    assert "Hello" in response.json()["reply"]
