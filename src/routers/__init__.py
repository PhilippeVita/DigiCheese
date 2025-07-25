from fastapi import APIRouter 
from .router_client import router_client 
from .router_commande import router_commande 
from .router_detail_commande import router_detail_commande
from .router_objet import router_objet


global_router = APIRouter(prefix="/api") 
global_router.include_router(router_client, prefix="/clients", tags=["clients"]) 
global_router.include_router(router_commande, prefix="/commandes", tags=["commandes"]) 
global_router.include_router(router_detail_commande, prefix="/details_commande", tags=["details_commande"]) 
global_router.include_router(router_objet, prefix="/objets", tags=["objets"]) 