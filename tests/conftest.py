import os
import sys
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
from datetime import date


# Ajout du dossier source au path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models import Client, Commande, DetailCommande, Objet, Commune, Departement
from src.main import app
from src.database import get_session

# Chargement des variables d’environnement
load_dotenv()

# URL de test (par défaut : SQLite en mémoire)
DATABASE_URL = os.getenv("TEST_DATABASE_URL", "sqlite:///:memory:")

# Création de l'engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


# --- Base de données & Session --- #
# Configuration de la base de données pour les tests
@pytest.fixture(scope="session")
def test_engine():
    SQLModel.metadata.create_all(engine)
    return engine

# --- Session de test --- #
@pytest.fixture
def test_session(test_engine):
    SQLModel.metadata.drop_all(test_engine)
    SQLModel.metadata.create_all(test_engine)
    with Session(test_engine) as session:
        yield session


# --- Override FastAPI dependency --- #

@pytest.fixture
def client(test_session):
    def override_get_session():
        yield test_session

    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


# --- Données de test --- #

@pytest.fixture
def departement_fixture(test_session):
    departement = Departement(code_dept="01", nom_dept="Ain", ordre_aff_dept=1)
    test_session.add(departement)
    test_session.commit()
    return departement

# Fixture pour la création d'une commune
@pytest.fixture
def commune_fixture(test_session, departement_fixture):
    commune = Commune(
        dep="01",
        cp="75000",
        ville="Paris"
    )
    test_session.add(commune)
    test_session.commit()
    test_session.refresh(commune)
    return commune

# Fixture pour la création d'un client
@pytest.fixture
def client_fixture(test_session, commune_fixture):
    client = Client(
        genrecli="M",
        nomcli="Client Test",
        prenomcli="Jean",
        adresse1cli="1 rue de Test",
        villecli_id=commune_fixture.id,
        telcli="0123456789",
        emailcli="client@example.com",
        newsletter=1
    )
    test_session.add(client)
    test_session.commit()
    test_session.refresh(client)
    return client

# Fixture pour la création d'une commande
@pytest.fixture
def test_commande(test_session, client_fixture):
    commande = Commande(
        codcli=client_fixture.codcli,
        datcde=date.today(),
        nbcolis=3,
        cdeComt="Test commande"
    )
    test_session.add(commande)
    test_session.commit()
    test_session.refresh(commande)
    return commande

# Fixture pour la création d'un objet
@pytest.fixture
def test_objet(test_session):
    objet = Objet(
        codobj=None,  
        libobj="Test Objet",
        description="Description de test",  
        puobj=10.0,
        indispobj=0,
        tailleobj=None,
        points=0,
        poidsobj=0,
        o_aff=0,
        o_cartp=0,
        o_ordre_aff=0,
        o_imp=0,
    )
    test_session.add(objet)
    test_session.commit()
    test_session.refresh(objet)
    return objet




# Fixture pour la création d'une commande
@pytest.fixture
def created_commande(test_session, client_fixture):
    commande = Commande(
        codcli=client_fixture.codcli,
        datcde=date.today(),
        nbcolis=3,
        cdeComt="Test commande"
    )
    test_session.add(commande)
    test_session.commit()
    test_session.refresh(commande)
    return commande

# Fixture pour la création d'un détail de commande
@pytest.fixture
def test_detail_commande(test_session, test_objet, test_commande):
    detail = DetailCommande(
        codcde=test_commande.codcde,
        codobj=test_objet.codobj,
        qte=2,
        colis=1
    )
    test_session.add(detail)
    test_session.commit()
    test_session.refresh(detail)
    return detail




















