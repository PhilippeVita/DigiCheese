from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlmodel import select, Session

from src.database import get_session
from src.models.commande import Commande, CommandePost, CommandePatch

router_commande = APIRouter()

@router_commande.get("/")
def get_all_commandes(session: Session = Depends(get_session)):
    commandes = session.exec(select(Commande)).all()
    data = jsonable_encoder(commandes)
    return JSONResponse(content={"data": data})

@router_commande.get("/{commande_id}")
def get_commande(commande_id: int, session: Session = Depends(get_session)):
    commande = session.get(Commande, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return JSONResponse(content=jsonable_encoder(commande))

@router_commande.post("/", status_code=status.HTTP_201_CREATED)
def create_commande(commande_post: CommandePost, session: Session = Depends(get_session)):
    commande_data = commande_post.model_dump(exclude_unset=True)
    commande = Commande(**commande_data)
    session.add(commande)
    session.commit()
    session.refresh(commande)
    return commande

@router_commande.patch("/{commande_id}")
def update_commande(commande_id: int, commande_patch: CommandePatch, session: Session = Depends(get_session)):
    commande = session.get(Commande, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")

    patch_data = commande_patch.model_dump(exclude_unset=True)
    for key, value in patch_data.items():
        setattr(commande, key, value)

    session.add(commande)
    session.commit()
    session.refresh(commande)
    return commande

@router_commande.delete("/{commande_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_commande(commande_id: int, session: Session = Depends(get_session)):
    commande = session.get(Commande, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    session.delete(commande)
    session.commit()
    return None
