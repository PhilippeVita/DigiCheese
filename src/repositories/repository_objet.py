from ..models import Objet, ObjetPost, ObjetPatch
from sqlmodel import Session, select

# classe RepositoryObjet
# Cette classe gère les opérations de base de données pour les objets
class RepositoryObjet:
    def __init__(self, session: Session):
        self.session = session

# Méthodes CRUD pour les objets
# Récupère tous les objets avec une limite sur le nombre de résultats
    def get_all_objets(self):
        statement= select(Objet)
        return self.session.exec(statement).all()

# Récupère un objet par son identifiant
    def get_objet_by_id(self, objet_id: int):
        statement = select(Objet).where(Objet.id == objet_id)
        return self.session.exec(statement).first()

# Crée un nouvel objet
    def create_objet(self, objet_data: ObjetPost):
        objet = Objet.model_validate(objet_data)
        self.session.add(objet)
        self.session.commit()
        self.session.refresh(objet)
        return objet

# Met à jour un objet existant
    def update_objet(self, objet_id: int, objet_data: ObjetPatch):
        objet = self.get_objet_by_id(objet_id)
        if not objet:
            return None
        for key, value in objet_data.model_dump(exclude_unset=True).items():
            setattr(objet, key, value)
        self.session.commit()
        self.session.refresh(objet)
        return objet

# Supprime un objet par son identifiant
    def delete_objet(self, objet_id: int):
        objet = self.get_objet_by_id(objet_id)
        if not objet:
            return None
        self.session.delete(objet)
        self.session.commit()
        return True