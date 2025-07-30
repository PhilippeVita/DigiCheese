from decimal import Decimal  
from typing import List
from sqlmodel import SQLModel, Field
from typing import Optional



class ObjetBase(SQLModel):
    """Schema de base representant les objets disponibles dans la fromagerie."""
    libobj: Optional[str] = Field(default=None, max_length=50, nullable=True)
    tailleobj: Optional[str] = Field(default=None, max_length=50, nullable=True)
    puobj: Decimal = Field(default=Decimal("0.0000"), nullable=False)
    poidsobj: Decimal = Field(default=Decimal("0.0000"), nullable=False)
    indispobj: Optional[int] = Field(default=0)
    o_imp: Optional[int] = Field(default=0)
    o_aff: Optional[int] = Field(default=0)
    o_cartp: Optional[int] = Field(default=0)
    points: Optional[int] = Field(default=0)
    o_ordre_aff: Optional[int] = Field(default=0)


class Objet(ObjetBase, table=True):
    """Table representant les objets disponibles dans la fromagerie."""
    __tablename__ = "t_objet"
    codobj: int | None = Field(default=None, primary_key=True)


class ObjetPost(ObjetBase):
    """Schema de validation pour la creation d'un nouvel objet."""
    pass


class ObjetPatch(ObjetBase):
    """Schema de validation pour la mise à jour d'un objet existant."""
    libobj: Optional[str] = Field(default=None, max_length=50, nullable=True)
    tailleobj: Optional[str] = Field(default=None, max_length=50, nullable=True)
    puobj: Optional[Decimal] = Field(default=Decimal("0.0000"), nullable=False)
    poidsobj: Optional[Decimal] = Field(default=Decimal("0.0000"), nullable=False)
    indispobj: Optional[int] = Field(default=0)
    o_imp: Optional[int] = Field(default=0)
    o_aff: Optional[int] = Field(default=0)
    o_cartp: Optional[int] = Field(default=0)
    points: Optional[int] = Field(default=0)
    o_ordre_aff: Optional[int] = Field(default=0)
    
