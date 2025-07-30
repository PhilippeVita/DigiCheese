from sqlmodel import SQLModel, Field
from typing import Optional

class DetailCommandeBase(SQLModel):
    """Schéma de base représentant les détails d'une commande."""
    qte: Optional[int] = Field(default=1, nullable=True)
    codcde: Optional[int] = Field(foreign_key="t_entcde.codcde")
    codobj: Optional[int] = Field(foreign_key="t_objet.codobj")  
    colis: Optional[int] = Field(default=1, nullable=True)
    commentaire: Optional[str] = Field(default=None, max_length=100, nullable=True)

class DetailCommande(DetailCommandeBase, table=True):
    """Table représentant les détails d'une commande."""
    __tablename__ = "t_dticode"
    id: Optional[int] = Field(default=None, primary_key=True)

class DetailCommandePost(DetailCommandeBase):
    """Schéma de validation pour la création d'un nouveau détail de commande."""
    pass

class DetailCommandePatch(DetailCommandeBase):
    """Schéma de validation pour la mise à jour d'un détail de commande existant."""
    pass



