from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app) # request

def test_get_home():
    response = client.get("/")
    assert response.status_code == 200
