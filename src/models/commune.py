from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from src.models.departement import Departement

class CommuneBase(SQLModel):
    """Schema de base representant les communes."""
    dep: str = Field(foreign_key="t_dept.code_dept", max_length=2, nullable=False)
    cp: Optional[str] = Field(default=None, max_length=5, nullable=True)
    ville: Optional[str] = Field(default=None, max_length=50, nullable=True)

class Commune(CommuneBase, table=True):
    """Table representant les communes."""
    __tablename__ = "t_communes"
    id: Optional[int] = Field(default=None, primary_key=True)
    departement: Optional[Departement] = Relationship(back_populates="communes")

class CommunePost(CommuneBase):
    """Schema de validation pour la creation d'une nouvelle commune."""
    pass

class CommunePatch(CommuneBase):
    """Schema de validation pour la mise a jour d'une commune existante."""
    pass
