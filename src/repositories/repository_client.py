from typing import Optional, List
from ..models.client import Client
from sqlmodel import Session, select

class RepositoryClient:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_by_id(self, client_id: int) -> Optional[Client]:
        statement = select(Client).where(Client.id == client_id)
        result = self.db_session.exec(statement)
        return result.first()

    def get_all(self) -> List[Client]:
        statement = select(Client)
        result = self.db_session.exec(statement)
        return result.all()

    def add(self, client: Client) -> Client:
        self.db_session.add(client)
        self.db_session.commit()
        self.db_session.refresh(client)
        return client

    def update(self, client: Client) -> Client:
        self.db_session.merge(client)
        self.db_session.commit()
        return client

    def delete(self, client: Client) -> None:
        self.db_session.delete(client)
        self.db_session.commit()
