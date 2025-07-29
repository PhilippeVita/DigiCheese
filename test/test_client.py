import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    return TestClient(app)

BASE_URL = "/api/clients"
  # Endpoint de ton API

def test_create_client(client, commune_fixture):
    payload = {
        "genrecli": "M",
        "nomcli": "New Client",
        "prenomcli": "Jean",
        "adresse1cli": "123 rue Exemple",
        "villecli_id": commune_fixture.id,
        "telcli": "0123456789",
        "emailcli": "newclient@example.com",
        "newsletter": False
    }
    response = client.post(BASE_URL, json=payload)
    assert response.status_code == 201
    assert response.json()["nomcli"] == "New Client"

def test_get_all_clients(client, test_client):
    response = client.get(BASE_URL)
    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert data["results"] == len(data["data"])
    assert any(cli["nomcli"] == "Test Client" for cli in data["data"])

# Tests commentés...
# def test_get_client_by_id(client, test_client):
#     ...

# def test_delete_client(client, test_client):
#     ...
