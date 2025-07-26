from sqlmodel import Session 
from ..repositories import RepositoryClient 
from ..models import ClientPost, ClientPatch, Client 
# Classe ClientService
# Cette classe encapsule la logique métier pour les opérations sur les clients
class ClientService: 
    def __init__(self, session: Session): 
        # Initialise le repository avec la session de base de données
        self.repository = RepositoryClient(session) 

    def __traitement(self, client: Client) -> Client:
        """
        Applique des transformations sur les données du client :
        - Met la première lettre du prénom en majuscule
        - Met le nom en majuscules
        """
        data = client.model_dump()
        data["prenom"] = data["prenom"].capitalize()
        data["nom"] = data["nom"].upper()
        return Client(**data)

    def trier_clients_par_ville(self, clients: Client) -> Client:
        """
        Trie la liste des clients par identifiant de ville (villecli_id).
        Les clients sans villecli_id sont placés en premier.
        """
        return sorted(clients, key=lambda client: client.villecli_id if client.villecli_id else 0)

    def trier_clients_par_nom(self, clients: Client) -> Client:
        """
        Trie la liste des clients par nom (ordre alphabétique, insensible à la casse).
        """
        return sorted(clients, key=lambda client: client.nom.lower())

    def get_all(self, limit: int): 
        """
        Récupère tous les clients (limite le nombre de résultats).
        """
        return self.repository.get_all(ClientPost, limit) 

    def create(self, data_client: ClientPost): 
        """
        Crée un nouveau client après traitement des données.
        """
        data_traite = self.__traitement(data_client) 
        return self.repository.create(data_traite) 
    
    def update(self, id: int, data_client: ClientPatch):
        """
        Met à jour un client existant après traitement des données.
        """
        data_traite = self.__traitement(data_client.model_dump())
        return self.repository.update(id, data_traite)
    