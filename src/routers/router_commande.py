from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from ..models import Commande, CommandePost, CommandePatch
from ..database import get_db
from ..repositories import RepositoryCommande

router_commande = APIRouter()

@router_commande.get("/")
def get_commandes(session: Session = Depends(get_db)):
    repo = RepositoryCommande(session)
    commandes = repo.get_all_commandes()
    return {
        "results": len(commandes),
        "data": commandes
    }

@router_commande.get("/{id}")
def get_commande_by_id(id: int, session: Session = Depends(get_db)):
    repo = RepositoryCommande(session)
    commande = repo.get_commande_by_id(id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return commande

@router_commande.post("/", status_code=status.HTTP_201_CREATED)
def create_commande(commande: CommandePost, session: Session = Depends(get_db)):
    repo = RepositoryCommande(session)
    new_commande = repo.create_commande(commande)
    return new_commande

@router_commande.put("/{id}")
def update_commande(id: int, commande: CommandePatch, session: Session = Depends(get_db)):
    repo = RepositoryCommande(session)
    updated_commande = repo.update_commande(id, commande)
    if not updated_commande:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return updated_commande

@router_commande.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_commande(id: int, session: Session = Depends(get_db)):
    repo = RepositoryCommande(session)
    success = repo.delete_commande(id)
    if not success:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return None
