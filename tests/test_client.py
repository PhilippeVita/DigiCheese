

BASE_URL = "/api/v1/clients"

# Tests for the Client Router
def test_create_client(client, commune_fixture):
    payload = {
        "genrecli": "M",
        "nomcli": "New Client",
        "prenomcli": "Jean",
        "adresse1cli": "123 rue Exemple",
        "adresse2cli": None,
        "adresse3cli": None,
        "villecli_id": commune_fixture.id,
        "telcli": "0123456789",
        "emailcli": "newclient@example.com",
        "portcli": None,
        "newsletter": False
    }
    response = client.post(BASE_URL, json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["nomcli"] == "New Client"
    assert "codcli" in data

# Tests pour avoir tous les clients
def test_get_all_clients(client, client_fixture):
    response = client.get(BASE_URL)
    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert data["results"] == len(data["data"])
    assert any(cli["nomcli"] == "Client Test" for cli in data["data"])

# Tests pour récupérer un client par son ID
def test_get_client_by_id(client, client_fixture):
    response = client.get(f"{BASE_URL}/{client_fixture.codcli}")
    assert response.status_code == 200

    data = response.json()
    assert data["codcli"] == client_fixture.codcli
    assert data["nomcli"] == client_fixture.nomcli



# Tests pour mettre à jour un client
def test_delete_client(client, client_fixture):
    client_id = client_fixture.codcli

    # Suppression du client
    response = client.delete(f"{BASE_URL}/{client_id}")
    assert response.status_code == 200
    assert f"Client {client_id} supprimé" in response.json()["message"]

    # Vérifier que le client n'existe plus
    res = client.get(f"{BASE_URL}/{client_id}")
    assert res.status_code == 404




