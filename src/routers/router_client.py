from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session
from src.database import get_session
from ..repositories import RepositoryClient
from ..models import ClientPost, ClientPatch, Client

router_client = APIRouter()

# ROUTES
# Récupère tous les clients
@router_client.get("/")
def get_clients(limit: int = 10, db: Session = Depends(get_session)):
    client_repo = RepositoryClient(db)
    clients = client_repo.get_all_clients(limit=limit)

    serialized_clients = [client.model_dump() for client in clients]

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "success",
            "results": len(serialized_clients),
            "data": serialized_clients
        }
    )

# Récupère un client par son ID
# Cette méthode récupère un client spécifique par son identifiant
@router_client.get("/{client_id}", response_model=Client)
def get_client_by_id(client_id: int, session: Session = Depends(get_session)):
    client = session.get(Client, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


# Crée un nouveau client
# Cette méthode crée un nouveau client en appliquant des transformations sur les données
# Dans router
@router_client.post("/", status_code=status.HTTP_201_CREATED)
def create_client(client: ClientPost, session: Session = Depends(get_session)):
    client_repo = RepositoryClient(session)
    created_client = client_repo.create_client(client)
    return created_client.model_dump()

# Met à jour un client existant
# Cette méthode met à jour un client en appliquant des transformations sur les données
@router_client.patch("/{id}")
def patch_client(id: int, client: ClientPatch, session: Session = Depends(get_session)):
    client_repo = RepositoryClient(session)
    client_repo.update_client(id, client)
    return {"message": f"Client {id} mis à jour: {client}"}

# Supprime un client par son ID
# Cette méthode supprime un client spécifique par son identifiant
@router_client.delete("/{client_id}")
def delete_client(client_id: int, session: Session = Depends(get_session)):
    client = session.get(Client, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")

    session.delete(client)
    session.commit()
    return {"message": f"Client {client_id} supprimé"}

    
    