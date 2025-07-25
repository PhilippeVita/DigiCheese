from sqlmodel import Session 
from ..repositories import RepositoryClient 
from ..models import ClientPost, ClientPatch, Client 

class ClientService: 
    def __init__(self, session: Session): 
        self.repository = RepositoryClient(session) 

    def __traitement(self, client: Client) -> Client:
        # Transformation via model_dump()
        data = client.model_dump()
        data["prenom"] = data["prenom"].capitalize()
        data["nom"] = data["nom"].upper()
        return Client(**data)

    def get_all(self, limit: int): 
        return self.repository.get_all(ClientPost, limit) 

    def create(self, data_client: ClientPost): 
        data_traite = self.__traitement(data_client) 
        return self.repository.create(data_traite) 
    
    def update(self, id: int, data_client: ClientPatch):
        data_traite = self.__traitement(data_client.model_dump())
        return self.repository.update(id, data_traite)
    