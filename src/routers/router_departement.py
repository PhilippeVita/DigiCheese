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

# Récupère un département par son code
# Cette méthode récupère un département spécifique par son code
@router_departement.get("/{code_dept}")
def get_departement_by_id(code_dept: str, session: Session = Depends(get_session)):
    departement_repo = RepositoryDepartement(session)
    departement = departement_repo.get_departement_by_id(code_dept)
    if not departement:
        raise HTTPException(status_code=404, detail="Département not found")
    return departement

# Crée un nouveau département
# Cette méthode crée un nouveau département en appliquant des transformations sur les données
@router_departement.post("/", status_code=status.HTTP_201_CREATED)
def create_departement(departement: DepartementPost, session: Session = Depends(get_session)):
    departement_repo = RepositoryDepartement(session)
    created = departement_repo.create_departement(departement)
    return created

# Met à jour un département existant
# Cette méthode met à jour un département en appliquant des transformations sur les données
@router_departement.patch("/{code_dept}")
def patch_departement(code_dept: str, departement: DepartementPatch, session: Session = Depends(get_session)):
    departement_repo = RepositoryDepartement(session)
    updated = departement_repo.update_departement(code_dept, departement)
    if not updated:
        raise HTTPException(status_code=404, detail="Département not found")
    return updated

# Supprime un département par son code
# Cette méthode supprime un département spécifique par son code
@router_departement.delete("/{code_dept}", status_code=status.HTTP_204_NO_CONTENT)
def delete_departement(code_dept: str, session: Session = Depends(get_session)):
    departement_repo = RepositoryDepartement(session)
    success = departement_repo.delete_departement(code_dept)
    if not success:
        raise HTTPException(status_code=404, detail="Département not found")
    return None
