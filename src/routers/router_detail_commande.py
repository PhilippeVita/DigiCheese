from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.responses import JSONResponse
from sqlmodel import Session

from ..models import DetailCommande, DetailCommandePost, DetailCommandePatch
from ..database import get_session
from ..repositories import RepositoryDetailCommande

# Ajout du prefix
router_detail_commande = APIRouter(
    prefix="/details-commandes",  
    tags=["detail-commandes"]
)



# Récupère tous les détails de commandes
@router_detail_commande.get("/")
def get_detail_commandes(session: Session = Depends(get_session)):
    repo = RepositoryDetailCommande(session)
    details = repo.get_all_detail_commandes()
    return {
        "status": "success",
        "results": len(details),
        "data": details
    }

# Récupère un détail de commande par ID
@router_detail_commande.get("/{id}")
def get_detail_commande_by_id(id: int, session: Session = Depends(get_session)):
    repo = RepositoryDetailCommande(session)
    detail = repo.get_detail_commande_by_id(id)
    if not detail:
        raise HTTPException(status_code=404, detail="DetailCommande not found")
    return detail

# Crée un nouveau détail de commande
@router_detail_commande.post("/", status_code=status.HTTP_201_CREATED)
def create_detail_commande(detail_data: DetailCommandePost, session: Session = Depends(get_session)):
    repo = RepositoryDetailCommande(session)
    detail = repo.create_detail_commande(detail_data)
    return detail

# Met à jour un détail de commande
@router_detail_commande.patch("/{id}")
def patch_detail_commande(id: int, detail_data: DetailCommandePatch, session: Session = Depends(get_session)):
    repo = RepositoryDetailCommande(session)
    detail = repo.update_detail_commande(id, detail_data)
    if not detail:
        raise HTTPException(status_code=404, detail="DetailCommande not found")
    return detail

#  Supprime un détail de commande
@router_detail_commande.delete("/{id}", status_code=204)
def delete_detail_commande(id: int, session: Session = Depends(get_session)):
    repo = RepositoryDetailCommande(session)
    success = repo.delete_detail_commande(id)
    if not success:
        raise HTTPException(status_code=404, detail="DetailCommande not found")
    return Response(status_code=204)




