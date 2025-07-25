# ------------------------------------------------------------------------------------
# Configuration des dépendances
# ------------------------------------------------------------------------------------

from fastapi import APIRouter
from .router_client import router_client
from .router_commande import router_commande
from .router_objet import router_objet
from .router_detail_commande import router_detail_commande

# ------------------------------------------------------------------------------------
# Routeurs
# ------------------------------------------------------------------------------------

router = APIRouter()

global_router = APIRouter(prefix="/api")
global_router.include_router(router_client, prefix="/clients", tags=["clients"])
global_router.include_router(router_commande, prefix="/commandes", tags=["commandes"])
global_router.include_router(router_objet, prefix="/objets", tags=["objets"])
global_router.include_router(router_detail_commande, prefix="/details_commande", tags=["details_commande"])
