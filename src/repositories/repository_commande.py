from typing import Optional, List
from ..models.commande import Commande
from sqlmodel import Session, select

class RepositoryCommande:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, commande_id: int) -> Optional[Commande]:
        statement = select(Commande).where(Commande.id == commande_id)
        result = self.session.exec(statement)
        return result.first()

    def add(self, commande: Commande) -> Commande:
        self.session.add(commande)
        self.session.commit()
        self.session.refresh(commande)
        return commande

    def delete(self, commande_id: int) -> bool:
        commande = self.get_by_id(commande_id)
        if commande:
            self.session.delete(commande)
            self.session.commit()
            return True
        return False

    def list_all(self) -> List[Commande]:
        statement = select(Commande)
        result = self.session.exec(statement)
        return result.all()
