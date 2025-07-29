from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session
from src.database import get_session
from ..repositories import RepositoryDepartement
from ..models import Departement, DepartementPost, DepartementPatch

router_departement = APIRouter()

# ROUTES
# Récupère tous les départements
@router_departement.get("/")
def get_departements(limit: int = 10, db: Session = Depends(get_session)):
    departement_repo = RepositoryDepartement(db)
    departements = departement_repo.get_all_departements(limit=limit)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "success",
            "results": len(departements),
            "data": departements
        }
    )

# Récupère un département par son ID
# Cette méthode récupère un département spécifique par son identifiant
@router_departement.get("/{id}")
def get_departement_by_id(id: int, session: Session = Depends(get_session)):
    departement_repo = RepositoryDepartement(session)
    departement = departement_repo.get_departement_by_id(id)
    if not departement:
        raise HTTPException(status_code=404, detail="Département not found")
    return departement

# Crée un nouveau département
# Cette méthode crée un nouveau département en appliquant des transformations sur les données
@router_departement.post("/")
def create_departement(departement: DepartementPost, session: Session = Depends(get_session)):
    departement_repo = RepositoryDepartement(session)
    departement_repo.create_departement(departement)
    return {"message": f"Département créé: {departement}"}

# Met à jour un département existant
# Cette méthode met à jour un département en appliquant des transformations sur les données
@router_departement.patch("/{id}")
def patch_departement(id: int, departement: DepartementPatch, session: Session = Depends(get_session)):
    departement_repo = RepositoryDepartement(session)
    departement_repo.update_departement(id, departement)
    return {"message": f"Département {id} mis à jour: {departement}"}

# Supprime un département par son ID
# Cette méthode supprime un département spécifique par son identifiant
@router_departement.delete("/{id}")
def delete_departement(id: int, session: Session = Depends(get_session)):
    departement_repo = RepositoryDepartement(session)
    departement_repo.delete_departement(id)
    return {"message": f"Département {id} supprimé"}
