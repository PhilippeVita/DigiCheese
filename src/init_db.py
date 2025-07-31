from sqlmodel import SQLModel
from src.database import engine
from src.models.client import Client  # importe tous les modèles utilisés

def init_db():
    print("Création des tables en cours...")
    SQLModel.metadata.create_all(engine)
    print("Tables créées avec succès !")

if __name__ == "__main__":
    init_db()
