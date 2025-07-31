from .client import Client, ClientPost, ClientPatch
from .commande import Commande, CommandePost, CommandePatch
from .detail_commande import DetailCommande, DetailCommandePost, DetailCommandePatch
from .objet import Objet, ObjetPost, ObjetPatch
from .commune import Commune, CommunePost, CommunePatch
from .departement import Departement, DepartementPost, DepartementPatch

__all__ = [
    "Client", "ClientPost", "ClientPatch",
    "Commande", "CommandePost", "CommandePatch",
    "DetailCommande", "DetailCommandePost", "DetailCommandePatch",
    "Objet", "ObjetPost", "ObjetPatch",
    "Commune", "CommunePost", "CommunePatch",
    "Departement", "DepartementPost", "DepartementPatch",
]
