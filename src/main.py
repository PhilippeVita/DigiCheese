from fastapi import FastAPI
from sqlmodel import SQLModel
from .database import engine
from .routers import global_router
from .models import (
    Client,
    Commande,
    Objet,
    DetailCommande,
)
# Initialisation de l'application FastAPI
app = FastAPI()
SQLModel.metadata.drop_all(bind=engine)
SQLModel.metadata.create_all(bind=engine)
app.include_router(global_router)
@app.get("/")
def read_root():
    return {"message": "Test de bon fonctionnement philippe , Nour et Ghassen 👍"} 

