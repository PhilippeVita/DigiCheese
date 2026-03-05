import os
from contextlib import asynccontextmanager
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

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: créer les tables uniquement si pas en mode test
    if os.getenv("TESTING") != "true":
        SQLModel.metadata.drop_all(bind=engine)
        SQLModel.metadata.create_all(bind=engine)
    yield
    # Shutdown: rien à faire ici

# Initialisation de l'application FastAPI
app = FastAPI(lifespan=lifespan)
app.include_router(global_router)

@app.get("/")
def read_root():
    return {"message": "Test de bon fonctionnement philippe , Nour et Ghassen"} 

