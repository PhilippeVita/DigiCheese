from sqlmodel import Session 
from ..repositories import RepositoryDepartement
from ..models import DepartementPost, DepartementPatch, Departement
from datetime import date

# Classe ServiceDepartement
# Cette classe applique des transformations et des règles métier pour les opérations sur les départements
class ServiceDepartement: 
    def __init__(self, session: Session): 
        self.repository = RepositoryDepartement(session) 

# Traitement des données du département
    def __traitement(self, departement: Departement) -> Departement: 
        data = departement.model_dump()
        data["date"] = data["date"].strftime("%Y-%m-%d")
        return Departement(**data)

# Trie les départements par date
    def trier_departements_par_date(self, departements: Departement) -> Departement:
        """
        Trie les départements par date.
        """
        return sorted(departements, key=lambda departement: departement.date)

# Trie les départements par client
    def trier_departements_par_client(self, departements: Departement) -> Departement:
        """
        Trie les départements par client.
        """
        return sorted(departements, key=lambda departement: departement.client.nom.lower() if departement.client else "")

 # Trie les départements par nombre de colis
    def trier_departements_par_nombre_colis(self, departements: Departement) -> Departement:
        """
        Trie les départements par nombre de colis.
        """
        return sorted(departements, key=lambda departement: departement.colis if departement.colis else 0)

# Récupère toutes les départements avec une limite
    def get_all(self, limit: int):
        return self.repository.get_all(DepartementPost, limit)

 # Crée une nouvelle département après traitement des données
    def create(self, data_departement: DepartementPost): 
        data_traite = self.__traitement(data_departement) 
        return self.repository.create(data_traite)

# Met à jour une département existante après traitement des données
    def update(self, id: int, data_departement: DepartementPatch):
        data_traite = self.__traitement(data_departement.model_dump())
        return self.repository.update(id, data_traite)

# Supprime une département par son ID
    def delete(self, id: int):
        return self.repository.delete(id)   