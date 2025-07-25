from typing import Optional, List
from ..models.objet import Objet
from sqlmodel import Session, select

class RepositoryObjet:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, objet_id: int) -> Optional[Objet]:
        statement = select(Objet).where(Objet.id == objet_id)
        result = self.session.exec(statement)
        return result.first()

    def get_all(self) -> List[Objet]:
        statement = select(Objet)
        result = self.session.exec(statement)
        return result.all()

    def add(self, objet: Objet) -> Objet:
        self.session.add(objet)
        self.session.commit()
        self.session.refresh(objet)
        return objet

    def update(self, objet: Objet) -> Objet:
        self.session.merge(objet)
        self.session.commit()
        return objet

    def delete(self, objet: Objet) -> None:
        self.session.delete(objet)
        self.session.commit()
