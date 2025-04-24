# tests/test_clients.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test creating a program
def test_create_program():
    response = client.post("/programs/", json={"name": "Malaria"})
    assert response.status_code == 200
    assert response.json()["name"] == "Malaria"

# Test creating a client
def test_create_client():
    response = client.post("/clients/", json={"name": "John Doe", "age": 30})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

# Test searching a client by name
def test_search_client():
    # Add a client for search
    client.post("/clients/", json={"name": "Jane Doe", "age": 25})
    response = client.get("/clients/?name=Jane")
    assert response.status_code == 200
    assert any("Jane" in client["name"] for client in response.json())

# Test enrolling a client into a program
def test_enroll_client():
    # Create a client and program first
    client_response = client.post("/clients/", json={"name": "Mark Smith", "age": 40})
    program_response = client.post("/programs/", json={"name": "HIV"})
    client_id = client_response.json()["id"]
    program_id = program_response.json()["id"]

    # Enroll client
    enroll_response = client.post(f"/clients/{client_id}/enroll", json=[program_id])
    assert enroll_response.status_code == 200
    assert "HIV" in [p["name"] for p in enroll_response.json()["programs"]]
