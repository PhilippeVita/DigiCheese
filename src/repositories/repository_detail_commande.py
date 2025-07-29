from ..models import DetailCommande, DetailCommandePost, DetailCommandePatch
from sqlmodel import Session, select
from fastapi import HTTPException

class RepositoryDetailCommande:
    def __init__(self, session: Session):
        self.session = session

    def get_all_detail_commandes(self):
        statement = select(DetailCommande)
        return self.session.exec(statement).all()

    def get_detail_commande_by_id(self, detail_commande_id: int) -> DetailCommande | None:
        statement = select(DetailCommande).where(DetailCommande.id == detail_commande_id)
        return self.session.exec(statement).first()

    def create_detail_commande(self, detail_commande_data: DetailCommandePost) -> DetailCommande:
        # Utilise model_validate pour convertir le Pydantic model en SQLModel
        detail_commande = DetailCommande.model_validate(detail_commande_data)
        self.session.add(detail_commande)
        self.session.commit()
        self.session.refresh(detail_commande)
        return detail_commande

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

    def delete_detail_commande(self, detail_commande_id: int) -> bool:
        detail_commande = self.get_detail_commande_by_id(detail_commande_id)
        if not detail_commande:
            return False
        self.session.delete(detail_commande)
        self.session.commit()
        return True

