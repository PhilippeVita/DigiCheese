from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING

# Éviter les importations circulaires en utilisant TYPE_CHECKING
if TYPE_CHECKING:
    from src.models.commune import Commune

class DepartementBase(SQLModel):
    """Schéma de base représentant un département."""
    nom_dept: Optional[str] = Field(default=None, max_length=50, nullable=True)
    ordre_aff_dept: int = Field(default=0)

class Departement(DepartementBase, table=True):
    __tablename__ = "t_dept"
    code_dept: str = Field(primary_key=True, max_length=2)  # renommé id -> code_dept
    
    communes: List["Commune"] = Relationship(back_populates="departement")


class DepartementPost(DepartementBase):
    """Schéma de validation pour la création d'un département."""
    code_dept: str = Field(..., max_length=2)

class DepartementPatch(DepartementBase):
    """Schéma de validation pour la mise à jour d'un département."""
    nom_dept: Optional[str] = Field(default=None, max_length=50)
    ordre_aff_dept: Optional[int] = Field(default=None)

class DepartementDelete(SQLModel):
    """Schéma pour la suppression d'un département."""
    code_dept: str = Field(..., max_length=2)

