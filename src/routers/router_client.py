from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from ..models import Client, ClientPost, ClientPatch
from ..database import get_db
from ..repositories import RepositoryClient

router_client = APIRouter()

@router_client.get("/")
def get_clients(session: Session = Depends(get_db)):
    repo = RepositoryClient(session)
    clients = repo.get_all_clients()
    return {
        "results": len(clients),
        "data": clients
    }

@router_client.get("/{id}")
def get_client_by_id(id: int, session: Session = Depends(get_db)):
    repo = RepositoryClient(session)
    client = repo.get_client_by_id(id)
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return client

@router_client.post("/", status_code=status.HTTP_201_CREATED)
def create_client(client: ClientPost, session: Session = Depends(get_db)):
    repo = RepositoryClient(session)
    new_client = repo.create_client(client)
    return new_client

@router_client.patch("/{id}")
def patch_client(id: int, client: ClientPatch, session: Session = Depends(get_db)):
    repo = RepositoryClient(session)
    updated_client = repo.update_client(id, client)
    if not updated_client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return updated_client

@router_client.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(id: int, session: Session = Depends(get_db)):
    repo = RepositoryClient(session)
    success = repo.delete_client(id)
    if not success:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return None
