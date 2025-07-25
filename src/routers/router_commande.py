from fastapi import APIRouter, Depends
from ..models import Commande, CommandePost, CommandePatch
from ..database import get_db
from sqlmodel import Session
from ..repositories import RepositoryCommande
router_commande = APIRouter()

# ROUTES
@router_commande.get("/")
def get_commandes(session: Session = Depends(get_db)):
    commande_repo = RepositoryCommande(session)
    return commande_repo.get_all_commandes()

@router_commande.get("/{id}")
def get_commande_by_id(id: int, session: Session = Depends(get_db)):
    commande_repo = RepositoryCommande(session)
    return commande_repo.get_commande_by_id(id)

@router_commande.post("/")
def create_commande(commande: CommandePost, session: Session = Depends(get_db)):
    commande_repo = RepositoryCommande(session)
    return commande_repo.create_commande(commande)

@router_commande.patch("/{id}")
def patch_commande(id: int, commande: CommandePatch, session: Session = Depends(get_db)):
    commande_repo = RepositoryCommande(session)
    return commande_repo.update_commande(id, commande)

@router_commande.delete("/{id}")
def delete_commande(id: int, session: Session = Depends(get_db)):
    commande_repo = RepositoryCommande(session)
    return commande_repo.delete_commande(id)