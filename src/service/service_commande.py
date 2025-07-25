from sqlmodel import Session 
from ..repositories import RepositoryCommande 
from ..models import CommandePost, CommandePatch 

class CommandeService: 
    def __init__(self, session: Session): 
        self.repository = RepositoryCommande(session) 

    def __traitement(self, commande): 
        commande.client.prenom = commande.client.prenom.capitalize()
        commande.client.nom = commande.client.nom.upper()
        return commande

    def get_all(self, limit: int): 
        return self.repository.get_all(CommandePost, limit) 

    def create(self, data_commande: CommandePost): 
        data_traite = self.__traitement(data_commande) 
        return self.repository.create(data_traite) 

    def update(self, id: int, data_commande: CommandePatch):
        data_traite = self.__traitement(data_commande.model_dump())
        return self.repository.update(id, data_traite)
    
    def delete(self, id: int):
        return self.repository.delete(id)   