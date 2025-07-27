from fastapi import APIRouter, Depends
from ..models import Commande, CommandePost, CommandePatch
from ..database import get_db
from sqlmodel import Session
from ..repositories import RepositoryCommande
router_commande = APIRouter()

# ROUTES
# Récupère toutes les commandes
@router_commande.get("/")
def get_commandes(session: Session = Depends(get_db)):
    commande_repo = RepositoryCommande(session)
    return commande_repo.get_all_commandes()

# Récupère une commande par son ID
# Cette méthode récupère une commande spécifique par son identifiant
@router_commande.get("/{id}")
def get_commande_by_id(id: int, session: Session = Depends(get_db)):
    commande_repo = RepositoryCommande(session)
    return commande_repo.get_commande_by_id(id)

# Crée une nouvelle commande
# Cette méthode crée une nouvelle commande en appliquant des transformations sur les données
@router_commande.post("/")
def create_commande(commande: CommandePost, session: Session = Depends(get_db)):
    commande_repo = RepositoryCommande(session)
    return commande_repo.create_commande(commande)

# Met à jour une commande existante
# Cette méthode met à jour une commande en appliquant des transformations sur les données
@router_commande.patch("/{id}")
def patch_commande(id: int, commande: CommandePatch, session: Session = Depends(get_db)):
    commande_repo = RepositoryCommande(session)
    return commande_repo.update_commande(id, commande)

# Supprime une commande par son ID
# Cette méthode supprime une commande spécifique par son identifiant
@router_commande.delete("/{id}")
def delete_commande(id: int, session: Session = Depends(get_db)):
    commande_repo = RepositoryCommande(session)
    return commande_repo.delete_commande(id)