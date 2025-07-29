from fastapi import Response

BASE_URL = "/api/v1/departements"

def test_get_all_departements(client):
    response: Response = client.get(BASE_URL)
    assert response.status_code == 200

def test_get_departement_by_id(client, departement_fixture):
    response: Response = client.get(f"{BASE_URL}/{departement_fixture.code_dept}")
    assert response.status_code == 200
    assert response.json()["nom_dept"] == "Ain"

def test_create_departement(client):
    data = {
        "code_dept": "02",
        "nom_dept": "Aisne",
        "ordre_aff_dept": 2
    }
    response: Response = client.post(BASE_URL, json=data)
    assert response.status_code == 201
    assert response.json()["nom_dept"] == "Aisne"

def test_update_departement(client, departement_fixture):
    data = {
        "nom_dept": "Ain Modifié",
        "ordre_aff_dept": 10
    }
    response: Response = client.put(f"{BASE_URL}/{departement_fixture.code_dept}", json=data)
    assert response.status_code == 200
    assert response.json()["nom_dept"] == "Ain Modifié"

def test_delete_departement(client, departement_fixture):
    response: Response = client.delete(f"{BASE_URL}/{departement_fixture.code_dept}")
    assert response.status_code == 204

    # Vérifie que le département a bien été supprimé
    response = client.get(f"{BASE_URL}/{departement_fixture.code_dept}")
    assert response.status_code == 404

