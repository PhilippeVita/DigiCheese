from decimal import Decimal  
from typing import List
from sqlmodel import SQLModel, Field

"""Schema de base representant les objets disponibles dans la fromagerie."""
class ObjetBase(SQLModel):
    libobj: str | None = Field(default=None, max_length=50, nullable=True)
    tailleobj: str | None = Field(default=None, max_length=50, nullable=True)
    puobj: Decimal = Field(default=Decimal("0.0000"), nullable=False)
    poidsobj: Decimal = Field(default=Decimal("0.0000"), nullable=False)
    indispobj: int = Field(default=0)
    o_imp: int = Field(default=0)
    o_aff: int = Field(default=0)
    o_cartp: int = Field(default=0)
    points: int = Field(default=0)
    o_ordre_aff: int = Field(default=0)

"""Table representant les objets disponibles dans la fromagerie."""
class Objet(ObjetBase, table=True):
    __tablename__ = "t_objet"
    codobj: int | None = Field(default=None, primary_key=True)

"""Schema de validation pour la creation d'un nouvel objet."""
class ObjetPost(ObjetBase):
    pass

"""Schema de validation pour la mise à jour d'un objet existant."""
class ObjetPatch(ObjetBase):
    pass
