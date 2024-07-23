from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_append_bananas():
    response = client.post("/append", json={"text": "Hello"})
    assert response.status_code == 200
    assert response.json() == {"result": "Hello bananas"}

def test_empty_input():
    response = client.post("/append", json={"text": ""})
    assert response.status_code == 200
    assert response.json() == {"result": " bananas"}

def test_special_characters():
    response = client.post("/append", json={"text": "Hello!@#"})
    assert response.status_code == 200
    assert response.json() == {"result": "Hello!@# bananas"}

def test_long_string():
    long_string = "a" * 1000
    response = client.post("/append", json={"text": long_string})
    assert response.status_code == 200
    assert response.json() == {"result": long_string + " bananas"}

