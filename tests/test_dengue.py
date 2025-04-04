import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "HDI API is running"}

def test_get_dengue_data():
    response = client.get("/dengue?limit=5&skip=0")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "data" in data
    assert len(data["data"]) == 5 

def test_filter_by_city():
    response = client.get("/dengue?city=Petrópolis")
    assert response.status_code == 200
    data = response.json()['data']
    print(data)
    assert all('Petrópolis' in str(record) for record in data)

def test_limit_and_skip():
    response = client.get("/dengue?limit=5&skip=10")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "data" in data
    assert len(data["data"]) == 5

def test_skip_greater_than_total():
    response = client.get("/dengue?limit=5&skip=8601")
    assert response.status_code == 200
    assert response.json()["data"] == []