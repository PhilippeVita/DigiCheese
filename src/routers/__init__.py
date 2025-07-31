from fastapi import APIRouter 
from .router_client import router_client 
from .router_commande import router_commande 
from .router_detail_commande import router_detail_commande
from .router_objet import router_objet
from .router_commune import router_commune
from .router_departement import router_departement


global_router = APIRouter(prefix="/api/v1") 
global_router.include_router(router_client, prefix="/clients", tags=["clients"]) 
global_router.include_router(router_commande, prefix="/commandes", tags=["commandes"]) 
global_router.include_router(router_detail_commande, prefix="/details-commandes", tags=["details-commandes"]) 
global_router.include_router(router_objet, prefix="/objets", tags=["objets"]) 
global_router.include_router(router_commune, prefix="/communes", tags=["communes"]) 
global_router.include_router(router_departement, prefix="/departements", tags=["departements"]) 