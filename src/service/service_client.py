from sqlmodel import Session 
from ..repositories import RepositoryClient 
from ..models import ClientPost, ClientPatch, Client 
# Classe ServiceClient
# Cette classe encapsule la logique métier pour les opérations sur les clients
class ServiceClient: 
    def __init__(self, session: Session): 
        # Initialise le repository avec la session de base de données
        self.repository = RepositoryClient(session) 
# Traitement des données du client
    # Cette méthode applique des transformations sur les données du client
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

    # Trie les clients par ville
    def trier_clients_par_ville(self, clients: Client) -> Client:
        """
        Trie la liste des clients par identifiant de ville (villecli_id).
        Les clients sans villecli_id sont placés en premier.
        """
        return sorted(clients, key=lambda client: client.villecli_id if client.villecli_id else 0)

# Trie les clients par nom
    # Cette méthode trie les clients par nom en ordre alphabétique, insensible à la
    def trier_clients_par_nom(self, clients: Client) -> Client:
        """
        Trie la liste des clients par nom (ordre alphabétique, insensible à la casse).
        """
        return sorted(clients, key=lambda client: client.nom.lower())

# Trie des clients par genre
    def trier_clients_par_genre(self, clients: Client) -> Client:
        """
        Trie la liste des clients par genre (genrecli).
        Les clients sans genrecli sont placés en premier.
        """
        return sorted(clients, key=lambda client: client.genrecli if client.genrecli else "")

# Recuperation des clients
    # Cette méthode récupère tous les clients avec une limite sur le nombre de résultats
    def get_all(self, limit: int): 
        """
        Récupère tous les clients (limite le nombre de résultats).
        """
        return self.repository.get_all(Client, limit) 
    
    # Récupère un client par son identifiant
    # Cette méthode récupère un client spécifique par son identifiant
    def get_by_id(self, id: int):
        """
        Récupère un client par son identifiant.
        """
        return self.repository.get_by_id(Client, id)

# Crée un nouveau client après traitement des données
    # Cette méthode crée un nouveau client en appliquant des transformations sur les données
    def create(self, data_client: ClientPost): 
        """
        Crée un nouveau client après traitement des données.
        """
        data_traite = self.__traitement(data_client) 
        return self.repository.create(data_traite) 

# Met à jour un client existant après traitement des données
    # Cette méthode met à jour un client en appliquant des transformations sur les données
    def update(self, id: int, data_client: ClientPatch):
        """
        Met à jour un client existant après traitement des données.
        """
        data_traite = self.__traitement(data_client.model_dump())
        return self.repository.update(id, data_traite)

# Supprime un client par son ID
    # Cette méthode supprime un client spécifique par son identifiant    
    def delete(self, id: int):
        """
        Supprime un client existant.
        """
        return self.repository.delete(id)
  