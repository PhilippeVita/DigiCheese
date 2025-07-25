from sqlmodel import SQLModel, Field

class DetailCommandeBase(SQLModel):
    """
        Schema de base representant les details des commandes.
    """
    codcde: int | None = Field(default=None, foreign_key="t_entcde.codcde", index=True, nullable=True)
    qte: int = Field(default=1, nullable=True)
    colis: int = Field(default=1, nullable=True)
    commentaire: str | None = Field(default=None, max_length=100, nullable=True)


class DetailCommande(DetailCommandeBase, table=True):
    """
        Table representant les details des commandes.
    """
    __tablename__ = "t_dticode"
    id: int | None = Field(default=None, primary_key=True)


class DetailCommandePost(DetailCommandeBase):
    pass


class DetailCommandePatch(DetailCommandeBase):
    codcde: int | None = Field(default=None, foreign_key="t_entcde.codcde", index=True, nullable=True)
    qte: int = Field(default=1, nullable=True)
    colis: int = Field(default=1, nullable=True)
    commentaire: str | None = Field(default=None, max_length=100, nullable=True)