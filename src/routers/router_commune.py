from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session
from src.database import get_session
from ..repositories import RepositoryCommune
from ..models import CommunePost, CommunePatch, Commune

router_commune = APIRouter()

# ROUTES
# Récupère toutes les communes
@router_commune.get("/")
def get_communes(limit: int = 10, db: Session = Depends(get_session)):
    commune_repo = RepositoryCommune(db)
    communes = commune_repo.get_all_communes(limit=limit)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "success",
            "results": len(communes),
            "data": communes
        }
    )

# Récupère une commune par son ID
# Cette méthode récupère une commune spécifique par son identifiant
@router_commune.get("/{id}")
def get_commune_by_id(id: int, session: Session = Depends(get_session)):
    commune_repo = RepositoryCommune(session)
    commune = commune_repo.get_commune_by_id(id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune

# Crée une nouvelle commune
# Cette méthode crée une nouvelle commune en appliquant des transformations sur les données
@router_commune.post("/")
def create_commune(commune: CommunePost, session: Session = Depends(get_session)):
    commune_repo = RepositoryCommune(session)
    commune_repo.create_commune(commune)
    return {"message": f"Commune créée: {commune}"}

# Met à jour une commune existante
# Cette méthode met à jour une commune en appliquant des transformations sur les données
@router_commune.patch("/{id}")
def patch_commune(id: int, commune: CommunePatch, session: Session = Depends(get_session)):
    commune_repo = RepositoryCommune(session)
    commune_repo.update_commune(id, commune)
    return {"message": f"Commune {id} mise à jour: {commune}"}

# Supprime une commune par son ID
# Cette méthode supprime une commune spécifique par son identifiant
@router_commune.delete("/{id}")
def delete_commune(id: int, session: Session = Depends(get_session)):
    commune_repo = RepositoryCommune(session)
    commune_repo.delete_commune(id)
    return {"message": f"Commune {id} supprimée"}