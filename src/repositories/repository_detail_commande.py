from ..models import DetailCommande, DetailCommandePost, DetailCommandePatch
from sqlmodel import Session, select
from fastapi import HTTPException
# RepositoryDetailCommande:
# Cette classe gère les opérations de base de données pour les détails de commande
class RepositoryDetailCommande:
    def __init__(self, session: Session):
        self.session = session
# Méthodes CRUD pour les détails de commande
    # Récupère tous les détails de commandes avec une limite sur le nombre de résultats
    def get_all_detail_commandes(self):
        statement = select(DetailCommande)
        return self.session.exec(statement).all()
# Récupère un détail de commande par son identifiant
    # Cette méthode récupère un détail de commande spécifique par son identifiant
    def get_detail_commande_by_id(self, detail_commande_id: int) -> DetailCommande | None:
        statement = select(DetailCommande).where(DetailCommande.id == detail_commande_id)
        return self.session.exec(statement).first()
# Crée un nouveau détail de commande
    # Cette méthode crée un nouveau détail de commande en appliquant des transformations sur les données
    def create_detail_commande(self, detail_commande_data: DetailCommandePost) -> DetailCommande:
        # Utilise model_validate pour convertir le Pydantic model en SQLModel
        detail_commande = DetailCommande.model_validate(detail_commande_data)
        self.session.add(detail_commande)
        self.session.commit()
        self.session.refresh(detail_commande)
        return detail_commande
# Met à jour un détail de commande existant
    # Cette méthode met à jour un détail de commande en appliquant des transformations sur les données
    def update_detail_commande(self, detail_commande_id: int, detail_commande_data: DetailCommandePatch) -> DetailCommande | None:
        detail_commande = self.get_detail_commande_by_id(detail_commande_id)
        if not detail_commande:
            return None
        # Met à jour uniquement les champs fournis
        for key, value in detail_commande_data.model_dump(exclude_unset=True).items():
            setattr(detail_commande, key, value)
        self.session.commit()
        self.session.refresh(detail_commande)
        return detail_commande
# Supprime un détail de commande par son identifiant
    # Cette méthode supprime un détail de commande spécifique par son identifiant
    def delete_detail_commande(self, detail_commande_id: int) -> bool:
        detail_commande = self.get_detail_commande_by_id(detail_commande_id)
        if not detail_commande:
            return False
        self.session.delete(detail_commande)
        self.session.commit()
        return True

