# commande.py
from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class CommandeBase(SQLModel):
    """Schema de base representant les commandes de la fromagerie."""
    datcde: Optional[date] = Field(default=None, nullable=True)
    codcli: Optional[int] = Field(default=None, foreign_key="t_client.codcli")
    timbrecli: Optional[float] = Field(default=None, nullable=True)
    timbrecde: Optional[float] = Field(default=None, nullable=True)
    nbcolis: Optional[int] = Field(default=1, nullable=True)
    cheqcli: Optional[float] = Field(default=None, nullable=True)
    idcondit: Optional[int] = Field(default=0, nullable=True)
    cdeComt: Optional[str] = Field(default=None, max_length=255, nullable=True)
    barchive: Optional[int] = Field(default=0, nullable=True)
    bstock: Optional[int] = Field(default=0, nullable=True)

class Commande(CommandeBase, table=True):
    """Table representant les commandes de la fromagerie."""
    __tablename__ = "t_entcde"
    codcde: Optional[int] = Field(default=None, primary_key=True)

    model_config = {
        "from_attributes": True
    }

class CommandePost(CommandeBase):
    """Schema de validation pour la creation d'une nouvelle commande."""
    pass

class CommandePatch(CommandeBase):
    """Schema de validation pour la mise a jour d'une commande existante."""
    pass
