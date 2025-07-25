from fastapi import APIRouter

router_detail_commande = APIRouter(prefix="/detail_commande")

# ROUTES
@router_detail_commande.get("/")
def get_detail_commande():
    return {"message": "Liste des details de la commande"}
 
@router_detail_commande.get("/{id}")
def get_detail_commande(id: int):
    return {"message": f"details de la commande avec l'ID {id}"}
 
@router_detail_commande.post("/")
def create_detail_commande(detail_commande: DetailPost):
    return {"message": f"details de la commande créé: {detail_commande}"}
 
@router_detail_commande.patch("/{id}")
def patch_detail_commande(id: int, detail_commande: DetailPatch):
    return {"message": f"details de la commande {id} mis à jour: {detail_commande}"}
 
@router_detail_commande.delete("/{id}")
def delete_detail_commande(id: int):
    return {"message": f"details de la commande {id} supprimé"}