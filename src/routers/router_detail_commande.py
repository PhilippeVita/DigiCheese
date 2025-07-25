from fastapi import APIRouter, Depends
from ..models import DetailCommande, DetailCommandePost, DetailCommandePatch
from ..database import get_db
from sqlmodel import Session
from ..repositories import RepositoryDetailCommande
router_detail_commande = APIRouter()

# ROUTES
@router_detail_commande.get("/")
def get_detail_commandes(session: Session = Depends(get_db)):
    detail_commande_repo = RepositoryDetailCommande(session)
    return detail_commande_repo.get_all_detail_commandes()

@router_detail_commande.get("/{id}")
def get_detail_commande_by_id(id: int, session: Session = Depends(get_db)):
    detail_commande_repo = RepositoryDetailCommande(session)
    return detail_commande_repo.get_detail_commande_by_id(id)

@router_detail_commande.post("/")
def create_detail_commande(detail_commande: DetailCommandePost, session: Session = Depends(get_db)):
    detail_commande_repo = RepositoryDetailCommande(session)
    return detail_commande_repo.create_detail_commande(detail_commande)

@router_detail_commande.patch("/{id}")
def patch_detail_commande(id: int, detail_commande: DetailCommandePatch, session: Session = Depends(get_db)):
    detail_commande_repo = RepositoryDetailCommande(session)
    return detail_commande_repo.update_detail_commande(id, detail_commande)

@router_detail_commande.delete("/{id}")
def delete_detail_commande(id: int, session: Session = Depends(get_db)):
    detail_commande_repo = RepositoryDetailCommande(session)
    return detail_commande_repo.delete_detail_commande(id)
    return client_repo.get_all_clients()
    

