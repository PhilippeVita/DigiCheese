from sqlmodel import Session 
from ..repositories import RepositoryObjet 
from ..models import ObjetPost, ObjetPatch, Objet
# Classe ServiceObjet
# Cette classe encapsule la logique métier pour les opérations sur les objets
class ServiceObjet: 
    def __init__(self, session: Session): 
        self.repository = RepositoryObjet(session) 
       
    # Traitement des données de l'objet
    def __traitement(self, objet: Objet) -> Objet: 
        data = objet.model_dump()
        data["date"] = data["date"].strftime("%Y-%m-%d")
        return Objet(**data)
    
    # Trie les objets par date
    def trier_objets_par_date(self, objets: list[Objet]) -> list[Objet]:
        return sorted(objets, key=lambda objet: objet.date)
    
    # Trie les objets par nom
    def trier_objets_par_nom(self, objets: list[Objet]) -> list[Objet]:
        return sorted(objets, key=lambda objet: objet.nom.lower() if objet.nom else "")
    
    # Trie les objets par taille, poids et points de fidélité
    def trier_objets_par_taille(self, objets: list[Objet]) -> list[Objet]:
        return sorted(objets, key=lambda objet: objet.taille if objet.taille else 0)
    
    # Trie les objets par poids
    def trier_objets_par_poids(self, objets: list[Objet]) -> list[Objet]:
        return sorted(objets, key=lambda objet: objet.poids if objet.poids else 0)
    
    # Trie les objets par points de fidélité
    def trier_objets_par_points_fidelite(self, objets: list[Objet]) -> list[Objet]:
        return sorted(objets, key=lambda objet: objet.points_fidelite if objet.points_fidelite else 0)
    
    # Récupère tous les objets avec une limite
    def get_all(self, limit: int):
        return self.repository.get_all(ObjetPost, limit)
    
    # Crée un nouvel objet après traitement des données
    def create(self, data_objet: ObjetPost): 
        data_traite = self.__traitement(data_objet) 
        return self.repository.create(data_traite)
    
    # Met à jour un objet existant après traitement des données
    def update(self, id: int, data_objet: ObjetPatch):
        data_traite = self.__traitement(data_objet.model_dump())
        return self.repository.update(id, data_traite)
    
    # Supprime un objet par son ID
    def delete(self, id: int):
        return self.repository.delete(id)   