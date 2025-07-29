from sqlmodel import SQLModel, Field
from typing import Optional

class DetailCommandeBase(SQLModel):
    qte: Optional[int] = Field(default=1, nullable=True)
    codcde: Optional[int] = Field(foreign_key="t_entcde.codcde")
    codobj: Optional[int] = Field(foreign_key="t_objet.codobj")  
    colis: Optional[int] = Field(default=1, nullable=True)
    commentaire: Optional[str] = Field(default=None, max_length=100, nullable=True)

class DetailCommande(DetailCommandeBase, table=True):
    __tablename__ = "t_dticode"
    id: Optional[int] = Field(default=None, primary_key=True)

class DetailCommandePost(DetailCommandeBase):
    pass

class DetailCommandePatch(DetailCommandeBase):
    pass



