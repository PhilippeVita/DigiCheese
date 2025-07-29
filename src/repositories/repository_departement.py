from ..models import Departement, DepartementPost, DepartementPatch
from sqlmodel import Session, select

#classe RepositoryDepartement
# Cette classe gère les opérations de base de données pour les départements
class RepositoryDepartement:
    def __init__(self, session: Session):
        self.session = session

# Méthodes CRUD pour les départements
# Récupère tous les départements avec une limite sur le nombre de résultats
    def get_all_departements(self, limit: int = 10):
        return self.session.exec(select(Departement).limit(limit)).all()

# Récupère un département par son identifiant
    def get_departement_by_id(self, departement_id: int):
        statement = select(Departement).where(Departement.id == departement_id)
        return self.session.exec(statement).first()

# Crée un nouveau département
    def create_departement(self, departement_data: DepartementPost):
        departement = Departement.model_validate(departement_data)
        self.session.add(departement)
        self.session.commit()
        self.session.refresh(departement)
        return departement

# Met à jour un département existant
    def update_departement(self, departement_id: int, departement_data: DepartementPatch):
        departement = self.get_departement_by_id(departement_id)
        if not departement:
            return None
        for key, value in departement_data.model_dump(exclude_unset=True).items():
            setattr(departement, key, value)
        self.session.commit()
        self.session.refresh(departement)
        return departement

# Supprime un département par son identifiant
    def delete_departement(self, departement_id: int):
        departement = self.get_departement_by_id(departement_id)
        if not departement:
            return None
        self.session.delete(departement)
        self.session.commit()
        return True
