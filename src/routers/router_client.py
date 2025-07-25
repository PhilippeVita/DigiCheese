# ==============================================================================
# Imports et configuration de la route Client
# ==============================================================================

from fastapi import APIRouter, Depends  # Système de routage FastAPI
from pydantic import BaseModel, Field, EmailStr # Modèles de validation pour les données clients
from sqlmodel import Session
from ..database import get_db
from typing import Optional


# ==============================================================================
# Initialisation du routeur pour l'entité Client
# ==============================================================================

router_client = APIRouter(
    prefix="/Client",
    tags=["Client"]
)

# ==============================================================================
# Modèles Pydantic pour POST et PATCH (si non importés depuis models/client.py)
# ==============================================================================

class ClientPost(BaseModel):
    genrecli: str = Field(..., max_length=8, description="Genre du client (ex: M, Mme)")
    nomcli: str = Field(..., max_length=40, description="Nom du client")
    prenomcli: str = Field(..., max_length=30, description="Prénom du client")
    adresselcli: Optional[str] = Field(None, max_length=50, description="Adresse ligne 1")
    adresse2cli: Optional[str] = Field(None, max_length=50, description="Adresse ligne 2")
    adresse3cli: Optional[str] = Field(None, max_length=50, description="Adresse ligne 3")
    villecli_id: Optional[int] = Field(None, description="ID de la ville (clé étrangère)")
    telcli: Optional[str] = Field(None, max_length=10, description="Numéro de téléphone fixe")
    emailcli: Optional[EmailStr] = Field(None, description="Adresse email du client")
    portcli: Optional[str] = Field(None, max_length=10, description="Numéro de téléphone portable")
    newsletter: Optional[int] = Field(None, description="Inscription à la newsletter (0 ou 1)")


class ClientPatch(BaseModel):
    genrecli: Optional[str] = Field(None, max_length=8, description="Genre du client")
    nomcli: Optional[str] = Field(None, max_length=40, description="Nom du client")
    prenomcli: Optional[str] = Field(None, max_length=30, description="Prénom du client")
    adresselcli: Optional[str] = Field(None, max_length=50, description="Adresse ligne 1")
    adresse2cli: Optional[str] = Field(None, max_length=50, description="Adresse ligne 2")
    adresse3cli: Optional[str] = Field(None, max_length=50, description="Adresse ligne 3")
    villecli_id: Optional[int] = Field(None, description="ID de la ville")
    telcli: Optional[str] = Field(None, max_length=10, description="Téléphone fixe")
    emailcli: Optional[EmailStr] = Field(None, description="Email")
    portcli: Optional[str] = Field(None, max_length=10, description="Téléphone portable")
    newsletter: Optional[int] = Field(None, description="Newsletter (0 ou 1)")


# ==============================================================================
# Endpoints CRUD pour l'entité Client
# ==============================================================================

@router_client.get("/")
def get_clients(db: Session = Depends(get_db)):
    """
        Récupérer la liste des clients.
    """
    pass

@router_client.get("/{id}")
def get_client_by_id(id: int, db: Session = Depends(get_db)):
    """
        Récupérer un client par son ID.
    """
    pass

@router_client.post("/", status_code=201)
def post_client(client: ClientPost, db: Session = Depends(get_db)):
    """
        Créer un nouveau client.
    """
    pass

@router_client.patch("/{id}")
def patch_client(id: int, client: ClientPatch, db: Session = Depends(get_db)):
    """
        Mettre à jour partiellement un client existant.
    """
    pass

@router_client.delete("/{id}", status_code=204)
def delete_client(id: int, db: Session = Depends(get_db)):
    """
        Supprimer un client par son ID.
    """
    pass

