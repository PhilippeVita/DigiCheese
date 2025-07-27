from sqlmodel import Session 
from ..repositories import RepositoryCommande 
from ..models import CommandePost, CommandePatch, Commande 

class ServiceCommande: 
    def __init__(self, session: Session): 
        self.repository = RepositoryCommande(session) 

# Traitement des données de la commande
    def __traitement(self, commande: Commande) -> Commande: 
        data = commande.model_dump()
        data["date"] = data["date"].strftime("%Y-%m-%d")
        return Commande(**data)

# Trie les commandes par date
    def trier_commandes_par_date(self, commandes: Commande) -> Commande:
        """
        Trie les commandes par date.
        """
        return sorted(commandes, key=lambda commande: commande.date)

# Trie les commandes par client
    def trier_commandes_par_client(self, commandes: Commande) -> Commande:
        """
        Trie les commandes par client.
        """
        return sorted(commandes, key=lambda commande: commande.client.nom.lower() if commande.client else "")

 # Trie les commandes par nombre de colis
    def trier_commandes_par_nombre_colis(self, commandes):
        """
        Trie les commandes par nombre de colis.
        """
        return sorted(commandes, key=lambda commande: commande.colis if commande.colis else 0)

# Récupère tous les commandes avec une limite
    def get_all(self, limit: int):
        return self.repository.get_all(CommandePost, limit)

 # Crée une nouvelle commande après traitement des données
    def create(self, data_commande: CommandePost): 
        data_traite = self.__traitement(data_commande) 
        return self.repository.create(data_traite)

# Met à jour une commande existante après traitement des données
    def update(self, id: int, data_commande: CommandePatch):
        data_traite = self.__traitement(data_commande.model_dump())
        return self.repository.update(id, data_traite)

# Supprime une commande par son ID
    def delete(self, id: int):
        return self.repository.delete(id)   