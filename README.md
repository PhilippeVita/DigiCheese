# 🧀 DigiCheese - API de gestion de fidélisation

DigiCheese est une API REST construite avec **FastAPI** et **SQLModel** pour gérer la fidélisation client d'une fromagerie. Elle permet de gérer les entités suivantes :

- Clients
- Commandes
- Détails de commande
- Objets
- Communes
- Départements

## 🚀 Technologies

- **FastAPI** - framework web asynchrone
- **SQLModel** - ORM basé sur SQLAlchemy et Pydantic
- **PyMySQL** - connecteur MySQL
- **pytest** - framework de tests
- **SQLite/MySQL** - bases de données

## 📦 Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-utilisateur/digicheese.git
cd digicheese

# 2. Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate   # ou .venv\Scripts\activate sous Windows

# 3. Installer les dépendances
pip install -r requirements.txt
```

## ⚙️ Configuration

Crée un fichier `.env` à la racine avec les variables suivantes :

```env
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/digicheese
TEST_DATABASE_URL=sqlite:///./test.db
```

## 🧪 Lancer les tests

```bash
pytest
```

> ⚠️ Par défaut, les tests utilisent la base de données définie dans `TEST_DATABASE_URL`.

## 📁 Structure du projet

```
digicheese/
│
├── src/
│   ├── main.py             # Point d’entrée de l’application FastAPI
│   ├── database.py         # Configuration de la base de données
│   ├── models/             # Définition des modèles SQLModel
│   │   ├── client.py
│   │   ├── commande.py
│   │   ├── detail_commande.py
│   │   ├── objet.py
│   │   ├── commune.py
│   │   └── departement.py
│   └── routers/            # Routes FastAPI (par entité)
│       ├── client_router.py
│       └── ...
│
├── tests/
│   ├── test_commande.py
│   ├── conftest.py
│   └── ...
│
├── .env                    # Variables d’environnement
├── requirements.txt        # Dépendances Python
└── README.md               # Ce fichier
```

## 🔧 Endpoints principaux

Quelques exemples d'URL :

- `GET /api/v1/clients/`
- `POST /api/v1/commandes/`
- `GET /api/v1/objets/{id}`
- `PATCH /api/v1/detail_commandes/{id}`

## 🤝 Contribuer

Les contributions sont bienvenues ! Pour contribuer :

1. Fork ce repo
2. Crée une branche (`git checkout -b feature/ma-feature`)
3. Commits tes changements (`git commit -am 'Ajout de ma feature'`)
4. Push ta branche (`git push origin feature/ma-feature`)
5. Crée une Pull Request

---


