from fastapi import APIRouter, Depends
from ..models import Client, ClientPost, ClientPatch
from ..database import get_db
from sqlmodel import Session
from ..repositories import RepositoryClient
router_client = APIRouter()

# ROUTES
@router_client.get("/")
def get_clients(session: Session = Depends(get_db)):
    client_repo = RepositoryClient(session)
    return client_repo.get_all_clients()
    

@router_client.get("/{id}")
def get_client_by_id(id: int, session: Session = Depends(get_db)):
    return {"message": f"Client avec l'ID {id}"}
 
@router_client.post("/")
def create_client(client: ClientPost, session: Session = Depends(get_db)):
    return {"message": f"Client créé: {client}"}
 
@router_client.patch("/{id}")
def patch_client(id: int, client: ClientPatch, session: Session = Depends(get_db)):
    return {"message": f"Client {id} mis à jour: {client}"}
 
@router_client.delete("/{id}")
def delete_client(id: int, session: Session = Depends(get_db)):
    return {"message": f"Client {id} supprimé"}
    
    