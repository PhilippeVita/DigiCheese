from ..models import Commande, CommandePost, CommandePatch
from sqlmodel import Session, select

# classe RepositoryCommande
# Cette classe gère les opérations de base de données pour les commandes
class RepositoryCommande:
    def __init__(self, session: Session):
        self.session = session

# Méthodes CRUD pour les commandes
# Récupère toutes les commandes
    def get_all_commandes(self):
        statement= select(Commande)
        return self.session.exec(statement).all()

# Récupère une commande par son identifiant
    def get_commande_by_id(self, commande_id: int):
        statement = select(Commande).where(Commande.id == commande_id)
        return self.session.exec(statement).first()

# Crée une nouvelle commande
    def create_commande(self, commande_data: CommandePost):
        commande = Commande.model_validate(commande_data)
        self.session.add(commande)
        self.session.commit()
        self.session.refresh(commande)
        return commande

# Met à jour une commande existante
    def update_commande(self, commande_id: int, commande_data: CommandePatch):
        commande = self.get_commande_by_id(commande_id)
        if not commande:
            return None
        for key, value in commande_data.model_dump(exclude_unset=True).items():
            setattr(commande, key, value)
        self.session.commit()
        self.session.refresh(commande)
        return commande

# Supprime une commande par son identifiant
    def delete_commande(self, commande_id: int):
        commande = self.get_commande_by_id(commande_id)
        if not commande:
            return None
        self.session.delete(commande)
        self.session.commit()
        return True