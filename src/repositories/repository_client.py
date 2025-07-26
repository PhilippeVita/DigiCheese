from ..models import Client, ClientPost, ClientPatch
from sqlmodel import Session, select
#classe RepositoryClient
# Cette classe gère les opérations de base de données pour les clients
class RepositoryClient:
    def __init__(self, session: Session):
        self.session = session
# Méthodes CRUD pour les clients
# Récupère tous les clients avec une limite sur le nombre de résultats
    def get_all_clients(self, limit: int):
        return self.session.exec(Client).limit(limit).all()
# Récupère un client par son identifiant
    def get_client_by_id(self, client_id: int):
        statement = select(Client).where(Client.id == client_id)
        return self.session.exec(statement).first()
# Crée un nouveau client
    def create_client(self, client_data: ClientPost):
        client = Client.model_validate(client_data)
        self.session.add(client)
        self.session.commit()
        self.session.refresh(client)
        return client
# Met à jour un client existant
    def update_client(self, client_id: int, client_data: ClientPatch):
        client = self.get_client_by_id(client_id)
        if not client:
            return None
        for key, value in client_data.model_dump(exclude_unset=True).items():
            setattr(client, key, value)
        self.session.commit()
        self.session.refresh(client)
        return client
# Supprime un client par son identifiant
    def delete_client(self, client_id: int):
        client = self.get_client_by_id(client_id)
        if not client:
            return None
        self.session.delete(client)
        self.session.commit()
        return True