from sqlmodel import Session 
from ..repositories import RepositoryCommune
from ..models import CommunePost, CommunePatch, Commune
from datetime import date

# Classe ServiceCommune
# Cette classe applique des transformations et des règles métier pour les opérations sur les communes
class ServiceCommune: 
    def __init__(self, session: Session): 
        self.repository = RepositoryCommune(session) 

# Traitement des données de la commune
    def __traitement(self, commune: Commune) -> Commune: 
        data = commune.model_dump()
        data["date"] = data["date"].strftime("%Y-%m-%d")
        return Commune(**data)

# Trie les communes par date
    def trier_communes_par_date(self, communes: Commune) -> Commune:
        """
        Trie les communes par date.
        """
        return sorted(communes, key=lambda commune: commune.date)

# Trie les communes par client
    def trier_communes_par_client(self, communes: Commune) -> Commune:
        """
        Trie les communes par client.
        """
        return sorted(communes, key=lambda commune: commune.client.nom.lower() if commune.client else "")

 # Trie les communes par nombre de colis
    def trier_communes_par_nombre_colis(self, communes):
        """
        Trie les communes par nombre de colis.
        """
        return sorted(communes, key=lambda commune: commune.colis if commune.colis else 0)

# Récupère toutes les communes avec une limite
    def get_all(self, limit: int):
        return self.repository.get_all(CommunePost, limit)

 # Crée une nouvelle commune après traitement des données
    def create(self, data_commune: CommunePost): 
        data_traite = self.__traitement(data_commune) 
        return self.repository.create(data_traite)

# Met à jour une commune existante après traitement des données
    def update(self, id: int, data_commune: CommunePatch):
        data_traite = self.__traitement(data_commune.model_dump())
        return self.repository.update(id, data_traite)

# Supprime une commune par son ID
    def delete(self, id: int):
        return self.repository.delete(id)   