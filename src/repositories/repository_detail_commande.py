from typing import Optional, List
from ..models.detail_commande import DetailCommande
from sqlmodel import Session, select

class RepositoryDetailCommande:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, detail_commande_id: int) -> Optional[DetailCommande]:
        statement = select(DetailCommande).where(DetailCommande.id == detail_commande_id)
        result = self.session.exec(statement)
        return result.first()

    def get_all(self) -> List[DetailCommande]:
        statement = select(DetailCommande)
        result = self.session.exec(statement)
        return result.all()

    def add(self, detail_commande: DetailCommande) -> DetailCommande:
        self.session.add(detail_commande)
        self.session.commit()
        self.session.refresh(detail_commande)
        return detail_commande

    def update(self, detail_commande: DetailCommande) -> DetailCommande:
        self.session.merge(detail_commande)
        self.session.commit()
        return detail_commande

    def delete(self, detail_commande: DetailCommande) -> None:
        self.session.delete(detail_commande)
        self.session.commit()
