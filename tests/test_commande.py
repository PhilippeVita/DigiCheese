import pytest
from datetime import date

BASE_URL = "/api/v1/commandes"

@pytest.fixture
def commande_payload(client_fixture):
    return {
        "codcli": client_fixture.codcli,  # bien le codcli généré
        "datcde": str(date.today()),
        "nbcolis": 3,
        "cdeComt": "Test commande"
    }


@pytest.fixture
def created_commande(client, commande_payload):
    response = client.post(BASE_URL + "/", json=commande_payload)
    assert response.status_code == 201
    return response.json()

def test_create_commande(client, commande_payload):
    response = client.post(BASE_URL + "/", json=commande_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["codcli"] == commande_payload["codcli"]
    assert data["nbcolis"] == commande_payload["nbcolis"]

def test_get_all_commandes(client):
    response = client.get(BASE_URL + "/")
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_commande_by_id(client, created_commande):
    commande_id = created_commande["codcde"]
    response = client.get(f"{BASE_URL}/{commande_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["codcde"] == commande_id

def test_update_commande(client, created_commande):
    commande_id = created_commande["codcde"]
    payload = {
        "nbcolis": 5,
        "cdeComt": "Commande mise à jour"
    }
    response = client.patch(f"{BASE_URL}/{commande_id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["nbcolis"] == 5
    assert data["cdeComt"] == "Commande mise à jour"

def test_delete_commande(client, created_commande):
    commande_id = created_commande["codcde"]
    response = client.delete(f"{BASE_URL}/{commande_id}")
    assert response.status_code == 204

    response = client.get(f"{BASE_URL}/{commande_id}")
    assert response.status_code == 404














