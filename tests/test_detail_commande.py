from fastapi import Response

BASE_URL = "/api/v1/details-commandes"
# Tests pour le Router Détail Commande
def test_create_detail_commande(client, test_commande, test_objet):
    response: Response = client.post(BASE_URL, json={
        "codcde": test_commande.codcde,
        "codobj": test_objet.codobj,
        "qte": 3
    })
    assert response.status_code == 201

    data = response.json()
    assert data["qte"] == 3
    assert data["codcde"] == test_commande.codcde
    assert data["codobj"] == test_objet.codobj

# Tests pour obtenir tous les détails de commande
def test_get_all_detail_commandes(client, test_detail_commande):
    response: Response = client.get(BASE_URL)
    assert response.status_code == 200

    # La liste des détails est dans 'data'
    data_list = response.json().get("data", [])
    assert any(d["id"] == test_detail_commande.id for d in data_list)

# Tests pour récupérer un détail de commande par son ID
def test_get_detail_commande_by_id(client, test_detail_commande):
    response: Response = client.get(f"{BASE_URL}/{test_detail_commande.id}")
    assert response.status_code == 200
    assert response.json()["id"] == test_detail_commande.id

# Tests pour mettre à jour un détail de commande
def test_update_detail_commande(client, test_detail_commande, test_objet):
    response: Response = client.patch(f"{BASE_URL}/{test_detail_commande.id}", json={
        "codcde": test_detail_commande.codcde,
        "codobj": test_objet.codobj,   
        "qte": 5
    })
    assert response.status_code == 200
    assert response.json()["qte"] == 5

# Tests pour supprimer un détail de commande
def test_delete_detail_commande(client, test_detail_commande):
    response = client.delete(f"{BASE_URL}/{test_detail_commande.id}")
    assert response.status_code == 204

    # Vérifie que la suppression a bien eu lieu
    response = client.get(f"{BASE_URL}/{test_detail_commande.id}")
    assert response.status_code == 404








