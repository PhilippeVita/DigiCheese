# ==============================================================================
# Imports et configuration
# ==============================================================================

from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from ..database import get_db
from ..models.detail_commande import DetailCommandePost, DetailCommandePatch

# ==============================================================================
# Initialisation du routeur pour l'entité DetailCommande
# ==============================================================================

router_detail_commande = APIRouter(
    prefix="/DetailCommande",
    tags=["DetailCommande"]
)

# ==============================================================================
# Endpoints CRUD pour l'entité DetailCommande
# ==============================================================================

@router_detail_commande.get("/", status_code=status.HTTP_200_OK)
def get_details_commandes(db: Session = Depends(get_db)):
    """
    Récupérer la liste des détails de commandes.
    """
    pass


@router_detail_commande.get("/{id}", status_code=status.HTTP_200_OK)
def get_detail_commande_by_id(id: int, db: Session = Depends(get_db)):
    """
    Récupérer un détail de commande par son ID.
    """
    pass


@router_detail_commande.post("/", status_code=status.HTTP_201_CREATED)
def post_detail_commande(detail: DetailCommandePost, db: Session = Depends(get_db)):
    """
    Créer un nouveau détail de commande.
    """
    pass


@router_detail_commande.patch("/{id}", status_code=status.HTTP_200_OK)
def patch_detail_commande(id: int, detail: DetailCommandePatch, db: Session = Depends(get_db)):
    """
    Mettre à jour partiellement un détail de commande existant.
    """
    pass


@router_detail_commande.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_detail_commande(id: int, db: Session = Depends(get_db)):
    """
    Supprimer un détail de commande par son ID.
    """
    pass
