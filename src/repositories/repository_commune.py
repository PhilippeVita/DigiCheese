from ..models import Commune, CommunePost, CommunePatch
from sqlmodel import Session, select

#classe RepositoryCommune
# Cette classe gère les opérations de base de données pour les communes
class RepositoryCommune:
    def __init__(self, session: Session):
        self.session = session

# Méthodes CRUD pour les communes
# Récupère toutes les communes avec une limite sur le nombre de résultats
    def get_all_communes(self, limit: int = 10):
        return self.session.exec(select(Commune).limit(limit)).all()

# Récupère une commune par son identifiant
    def get_commune_by_id(self, commune_id: int):
        statement = select(Commune).where(Commune.id == commune_id)
        return self.session.exec(statement).first()

# Crée une nouvelle commune
    def create_commune(self, commune_data: CommunePost):
        commune = Commune.model_validate(commune_data)
        self.session.add(commune)
        self.session.commit()
        self.session.refresh(commune)
        return commune

# Met à jour une commune existante
    def update_commune(self, commune_id: int, commune_data: CommunePatch):
        commune = self.get_commune_by_id(commune_id)
        if not commune:
            return None
        for key, value in commune_data.model_dump(exclude_unset=True).items():
            setattr(commune, key, value)
        self.session.commit()
        self.session.refresh(commune)
        return commune

# Supprime une commune par son identifiant
    def delete_commune(self, commune_id: int):
        commune = self.get_commune_by_id(commune_id)
        if not commune:
            return None
        self.session.delete(commune)
        self.session.commit()
        return True


