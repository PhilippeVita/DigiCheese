from fastapi import APIRouter, Depends
from ..models import Objet, ObjetPost, ObjetPatch
from ..database import get_db
from sqlmodel import Session
from ..repositories import RepositoryObjet
router_objet = APIRouter()

# ROUTES
@router_objet.get("/")
def get_objets(session: Session = Depends(get_db)):
    objet_repo = RepositoryObjet(session)
    return objet_repo.get_all_objets()

@router_objet.get("/{id}")
def get_objet_by_id(id: int, session: Session = Depends(get_db)):
    objet_repo = RepositoryObjet(session)
    return objet_repo.get_objet_by_id(id)

@router_objet.post("/")
def create_objet(objet: ObjetPost, session: Session = Depends(get_db)):
    objet_repo = RepositoryObjet(session)
    return objet_repo.create_objet(objet)

@router_objet.patch("/{id}")
def patch_objet(id: int, objet: ObjetPatch, session: Session = Depends(get_db)):
    objet_repo = RepositoryObjet(session)
    return objet_repo.update_objet(id, objet)

@router_objet.delete("/{id}")
def delete_objet(id: int, session: Session = Depends(get_db)):
    objet_repo = RepositoryObjet(session)
    return objet_repo.delete_objet(id)

    return client_repo.get_all_clients()
    