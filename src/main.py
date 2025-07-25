from fastapi import FastAPI
from sqlmodel import SQLModel
from .models import Client, Commande, DetailCommande, Objet
from .database import engine
from .models import (
    Client,
    Commande,
    Objet,
    DetailCommande,
)

app = FastAPI()
SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Test de bon fonctionnement philippe , Nour et Ghassen 👍"}