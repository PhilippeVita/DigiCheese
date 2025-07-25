# ==============================================================================
# Imports et configuration de la route Objet
# ==============================================================================

from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from ..database import get_db
from ..models.objet import ObjetPost, ObjetPatch

# ==============================================================================
# Initialisation du routeur pour l'entité Objet
# ==============================================================================

router_objet = APIRouter(
    prefix="/Objet",
    tags=["Objet"]
)

# ==============================================================================
# Endpoints CRUD pour l'entité Objet
# ==============================================================================

@router_objet.get("/", status_code=status.HTTP_200_OK)
def get_objets(db: Session = Depends(get_db)):
    """
    Récupérer la liste des objets.
    """
    pass


@router_objet.get("/{id}", status_code=status.HTTP_200_OK)
def get_objet_by_id(id: int, db: Session = Depends(get_db)):
    """
    Récupérer un objet par son ID.
    """
    pass


@router_objet.post("/", status_code=status.HTTP_201_CREATED)
def post_objet(objet: ObjetPost, db: Session = Depends(get_db)):
    """
    Créer un nouvel objet.
    """
    pass


@router_objet.patch("/{id}", status_code=status.HTTP_200_OK)
def patch_objet(id: int, objet: ObjetPatch, db: Session = Depends(get_db)):
    """
    Mettre à jour partiellement un objet existant.
    """
    pass


@router_objet.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_objet(id: int, db: Session = Depends(get_db)):
    """
    Supprimer un objet par son ID.
    """
    pass
