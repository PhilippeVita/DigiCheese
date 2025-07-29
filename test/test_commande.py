import pytest
from fastapi import Response
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    return TestClient(app)

BASE_URL = "/api/v1/commandes"

# Création d'une commande
def test_create_commande(client, test_client):
    response: Response = client.post(BASE_URL, json={"client_id": test_client.id})
    assert response.status_code == 201
    assert response.json()["client_id"] == test_client.id

# Récupération de toutes les commandes
def test_get_all_commandes(client, test_commande):
    response: Response = client.get(BASE_URL)
    assert response.status_code == 200
    assert any(c["id"] == test_commande.id for c in response.json())

# Récupération d'une commande par ID
def test_get_commande_by_id(client, test_commande):
    response: Response = client.get(f"{BASE_URL}/{test_commande.id}")
    assert response.status_code == 200
    assert response.json()["id"] == test_commande.id

# Mise à jour d'une commande
def test_update_commande(client, test_commande):
    response: Response = client.put(
        f"{BASE_URL}/{test_commande.id}", json={"client_id": test_commande.client_id}
    )
    assert response.status_code == 200
    assert response.json()["client_id"] == test_commande.client_id

# Suppression d'une commande
def test_delete_commande(client, test_commande):
    response: Response = client.delete(f"{BASE_URL}/{test_commande.id}")
    assert response.status_code == 204

    # Vérifie qu'elle n'existe plus
    response = client.get(f"{BASE_URL}/{test_commande.id}")
    assert response.status_code == 404
