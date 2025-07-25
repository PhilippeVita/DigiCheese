# ==============================================================================
# Imports et configuration de la route DetailCommande
# ==============================================================================

from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..repositories.repository_detail_commande import DetailCommande
from ..models.detail_commande import (
    DetailCommande,
    DetailCommandePost,
    DetailCommandePatch,
)

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

@router_detail_commande.get("/")
def get_detail_commande():
    """
        Récupérer toutes les lignes de détail de commande.
    """
    pass

@router_detail_commande.get("/{id}")
def get_detail_commande_by_id(id: int):
    """
        Récupérer une ligne de détail de commande par son ID.
    """
    pass

@router_detail_commande.post("/")
def post_detail_commande(detail_commande: DetailCommandePost):
    """
        Créer une nouvelle ligne de détail de commande.
    """
    pass

@router_detail_commande.patch("/{id}")
def patch_detail_commande(id: int, detail_commande: DetailCommandePatch):
    """
        Mettre à jour partiellement une ligne de détail de commande existante.
    """
    pass

@router_detail_commande.delete("/{id}")
def delete_detail_commande(id: int):
    """
        Supprimer une ligne de détail de commande par son ID.
    """
    pass
