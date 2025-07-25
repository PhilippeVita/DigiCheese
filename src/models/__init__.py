"""
Centralisation des imports des modèles du projet.

Ce fichier agit comme point d'entrée pour accéder aux classes des modèles :
Client, Objet, Commande, DetailCommande, ainsi que leurs variantes Post et Patch.
"""

from .client import Client, ClientPost, ClientPatch
from .objet import Objet, ObjetPost, ObjetPatch
from .commande import Commande, CommandePost, CommandePatch
from .detail_commande import DetailCommande, DetailCommandePost, DetailCommandePatch
