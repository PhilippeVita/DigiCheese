from fastapi import Response

BASE_URL = "/api/v1/objets"

# Tests pour le Router Objet
def test_create_objet(client):
    response: Response = client.post(BASE_URL, json={
        "libobj": "Objet Test",
        "tailleobj": "M",
        "puobj": 19.99,
        "poidsobj": 1.5,
        "indispobj": 0,
        "o_imp": 0,
        "o_aff": 0,
        "o_cartp": 0,
        "points": 0,
        "o_ordre_aff": 0
    })
    assert response.status_code == 201
    assert response.json()["libobj"] == "Objet Test"

# Tests pour obtenir tous les objets
def test_get_all_objets(client, test_objet):
    response: Response = client.get(BASE_URL)
    assert response.status_code == 200
    assert any(o["codobj"] == test_objet.codobj for o in response.json())

# Tests pour obtenir un objet par son ID
def test_get_objet_by_id(client, test_objet):
    response: Response = client.get(f"{BASE_URL}/{test_objet.codobj}")
    assert response.status_code == 200
    assert response.json()["codobj"] == test_objet.codobj

# Tests pour mettre à jour un objet
def test_update_objet(client, test_objet):
    response: Response = client.put(f"{BASE_URL}/{test_objet.codobj}", json={
        "libobj": "Objet Modifié",
        "tailleobj": "L",
        "puobj": 25.0,
        "poidsobj": 2.0,
        "indispobj": 0,
        "o_imp": 0,
        "o_aff": 0,
        "o_cartp": 0,
        "points": 0,
        "o_ordre_aff": 0
    })
    assert response.status_code == 200
    assert response.json()["libobj"] == "Objet Modifié"

# Tests pour supprimer un objet
def test_delete_objet(client, test_objet):
    response: Response = client.delete(f"{BASE_URL}/{test_objet.codobj}")
    assert response.status_code == 204

    response = client.get(f"{BASE_URL}/{test_objet.codobj}")
    assert response.status_code == 404

