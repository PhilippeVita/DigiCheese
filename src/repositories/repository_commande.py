from ..models import Commande, CommandePost, CommandePatch
from sqlmodel import Session, select

class RepositoryCommande:
    def __init__(self, session: Session):
        self.session = session

    def get_all_commandes(self):
        statement= select(Commande)
        return self.session.exec(statement).all()

    def get_commande_by_id(self, commande_id: int):
        statement = select(Commande).where(Commande.id == commande_id)
        return self.session.exec(statement).first()

    def create_commande(self, commande_data: CommandePost):
        commande = Commande.model_validate(commande_data)
        self.session.add(commande)
        self.session.commit()
        self.session.refresh(commande)
        return commande

    def update_commande(self, commande_id: int, commande_data: CommandePatch):
        commande = self.get_commande_by_id(commande_id)
        if not commande:
            return None
        for key, value in commande_data.model_dump(exclude_unset=True).items():
            setattr(commande, key, value)
        self.session.commit()
        self.session.refresh(commande)
        return commande

    def delete_commande(self, commande_id: int):
        commande = self.get_commande_by_id(commande_id)
        if not commande:
            return None
        self.session.delete(commande)
        self.session.commit()
        return True