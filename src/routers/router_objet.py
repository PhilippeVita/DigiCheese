from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from ..models import Objet, ObjetPost, ObjetPatch
from ..database import get_session
from sqlmodel import Session
from ..repositories import RepositoryObjet
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

router_objet = APIRouter()

# ROUTES
# Récupère tous les objets
# Cette méthode récupère tous les objets disponibles dans la base de données
@router_objet.get("/")
def get_objets(session: Session = Depends(get_session)):
    objet_repo = RepositoryObjet(session)
    objets = objet_repo.get_all_objets()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "success",
            "results": len(objets),
            "data": jsonable_encoder(objets)
        }
    )

# Récupère un objet par son ID
# Cette méthode récupère un objet spécifique par son identifiant
@router_objet.get("/{id}")
def get_objet_by_id(id: int, session: Session = Depends(get_session)):
    objet_repo = RepositoryObjet(session)
    objet = objet_repo.get_objet_by_id(id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet

# Crée un nouvel objet
# Cette méthode crée un nouvel objet en appliquant des transformations sur les données
@router_objet.post("/", status_code=status.HTTP_201_CREATED)
def create_objet(objet: ObjetPost, session: Session = Depends(get_session)):
    objet_repo = RepositoryObjet(session)
    return objet_repo.create_objet(objet)

# Met à jour un objet existant
# Cette méthode met à jour un objet en appliquant des transformations sur les données
@router_objet.patch("/{id}")
def patch_objet(id: int, objet: ObjetPatch, session: Session = Depends(get_session)):
    objet_repo = RepositoryObjet(session)
    return objet_repo.update_objet(id, objet)

# Supprime un objet par son ID
# Cette méthode supprime un objet spécifique par son identifiant
@router_objet.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_objet(id: int, session: Session = Depends(get_session)):
    objet_repo = RepositoryObjet(session)
    success = objet_repo.delete_objet(id)
    if not success:
        raise HTTPException(status_code=404, detail="Objet not found")
    return None
