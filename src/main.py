# ------------------------------------------------------------------------------------
#  Configuration des dépendances 
# ------------------------------------------------------------------------------------
from fastapi.responses import HTMLResponse
from fastapi import FastAPI     # Modèles
from sqlmodel import SQLModel   # Routeurs
from .models import Client      # Repositories
from .database import engine    # Data Base


"""from .models import (
    Departement,
    Commune,
    Client,
    Commande,
    Conditionnement,
    Objet,
    ObjetCond,
    Detail,
    DetailObjet,
    Enseigne,
    Poids,
    Role,
    Utilisateur,
    RoleUtilisateur
)
"""

app = FastAPI()
SQLModel.metadata.create_all(bind=engine)

# -- Configuration de la Route Swagger ( --> OpenAPI )

@app.get("/", response_class=HTMLResponse)  # def read_root():
def index():
    """  
        Configuration de OpenAPI ( <--- Swagger ) 
        -----------------------------------------
        Affichage d'un message par défaut
        URL : http(s)://127.0.0.1:800[0-9]/
    """
    message = (
        "Test de bon fonctionnement avec l'équipe 1 : <br>"
        "1 - Ghassen SOUISSI 👍<br>"
        "2 - Nour ZERABIB 👍<br>"
        "3 - Philippe VITA 👍<br>"
    )
    return f"<html><body><h3>{message}</h3></body></html>"