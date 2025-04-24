from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

#  Test cases
def test_get_200():
    response = client.get("/test/200")
    assert response.status_code == 200
    assert response.json() == {"data": "Success (Simulated)"}

def test_get_404():
    response = client.get("/test/404")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found (Simulated)"

def test_get_400():
    response = client.get("/test/400")
    assert response.status_code == 400
    assert response.json()["detail"] == "Bad Request (Simulated)"

def test_get_500():
    response = client.get("/test/500")
    assert response.status_code == 500
    assert response.json()["detail"] == "Internal Server Error (Simulated)"

def test_get_201():
    response = client.get("/test/201")
    assert response.status_code == 201
    assert response.json()["detail"] == "Created (Simulated)"