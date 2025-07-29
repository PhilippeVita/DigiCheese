from ..models import Client, ClientPost, ClientPatch
from sqlmodel import Session, select

class RepositoryClient:
    def __init__(self, session: Session):
        self.session = session

    def get_all_clients(self, limit: int = 10):
        return self.session.exec(select(Client).limit(limit)).all()

    def get_client_by_id(self, client_id: int):
        statement = select(Client).where(Client.id == client_id)
        return self.session.exec(statement).first()


    def create_client(self, client: ClientPost) -> Client:
        new_client = Client(**client.model_dump())
        self.session.add(new_client)
        self.session.commit()
        self.session.refresh(new_client)  
        return new_client

  

    def update_client(self, client_id: int, client_data: ClientPatch):
        client = self.get_client_by_id(client_id)
        if not client:
            return None
        for key, value in client_data.model_dump(exclude_unset=True).items():
            setattr(client, key, value)
        self.session.commit()
        self.session.refresh(client)
        return client

    def delete_client(self, client_id: int):
        client = self.get_client_by_id(client_id)
        if not client:
            return None
        self.session.delete(client)
        self.session.commit()
        return True