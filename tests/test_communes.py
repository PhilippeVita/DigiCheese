from fastapi import Response

BASE_URL = "/api/v1/communes"

def test_get_all_communes(client):
    response: Response = client.get(BASE_URL)
    assert response.status_code == 200

def test_get_commune_by_id(client, commune_fixture):
    response: Response = client.get(f"{BASE_URL}/{commune_fixture.id}")
    assert response.status_code == 200
    assert response.json()["ville"] == "Bourg-en-Bresse"

def test_create_commune(client, departement_fixture):
    data = {
        "dep": departement_fixture.code_dept,
        "cp": "01002",
        "ville": "Autre Ville"
    }
    response: Response = client.post(BASE_URL, json=data)
    assert response.status_code == 201
    assert response.json()["ville"] == "Autre Ville"

def test_update_commune(client, commune_fixture):
    data = {
        "dep": commune_fixture.dep,
        "cp": "01000",
        "ville": "Ville Modifiée"
    }
    response: Response = client.put(f"{BASE_URL}/{commune_fixture.id}", json=data)
    assert response.status_code == 200
    assert response.json()["ville"] == "Ville Modifiée"

def test_delete_commune(client, commune_fixture):
    response: Response = client.delete(f"{BASE_URL}/{commune_fixture.id}")
    assert response.status_code == 204

    # Vérifie que la commune a bien été supprimée
    response = client.get(f"{BASE_URL}/{commune_fixture.id}")
    assert response.status_code == 404

