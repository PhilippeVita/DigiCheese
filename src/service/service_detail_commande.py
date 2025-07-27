from sqlmodel import Session 
from ..repositories import RepositoryDetailCommande 
from ..models import DetailCommandePost, DetailCommandePatch, DetailCommande

# Traitement des données de detail de commande
class ServiceDetailCommande: 
    def __init__(self, session: Session): 
        self.repository = RepositoryDetailCommande(session) 
    
    # Applique des transformations sur les données de detail de commande    
    def __traitement(self, detail_commande: DetailCommande) -> DetailCommande: 
        data_detail = detail_commande.model_dump()
        data_detail["date"] = data_detail["date"].strftime("%Y-%m-%d")
        return DetailCommande(**data_detail)
    
    # Trie les detail de commandes par date
    def trier_detail_commandes_par_date(self, detail_commandes: DetailCommande) -> DetailCommande:
        return sorted(detail_commandes, key=lambda commande: commande.date)
    
    # Trie les detail de commandes par client
    def trier_detail_commandes_par_client(self, detail_commandes: DetailCommande) -> DetailCommande:
        return sorted(detail_commandes, key=lambda detail_commande: detail_commande.client.nom.lower() if detail_commande.client else "")
    
    # Trie les detail de commandes par nombre de colis
    def trie_detail_commandes_par_nombre_colis(self, detail_commandes: DetailCommande) -> DetailCommande:
        return sorted(detail_commandes, key=lambda detail_commande: detail_commande.colis if detail_commande.colis else 0)
    
    # Récupère tous les detail de commandes avec une limite
    def get_all(self, limit: int): 
        return self.repository.get_all(DetailCommandePost, limit) 
    
    # Crée un nouveau detail de commande après traitement des données
    def create(self, data_detail_commande: DetailCommandePost): 
        data_traite = self.__traitement(data_detail_commande) 
        return self.repository.create(data_traite)
   
    # Met à jour un detail de commande existant après traitement des données
    def update(self, id: int, data_detail_commande: DetailCommandePatch):
        data_traite = self.__traitement(data_detail_commande.model_dump())
        return self.repository.update(id, data_traite)
   
    # Supprime un detail de commande par son ID
    def delete(self, id: int):
        return self.repository.delete(id)   