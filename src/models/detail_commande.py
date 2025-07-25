from sqlmodel import SQLModel, Field
"""Schema de base representant les details des commandes."""
class DetailCommandeBase(SQLModel):
    codcde: int | None = Field(default=None, foreign_key="t_entcde.codcde", index=True, nullable=True)
    qte: int = Field(default=1, nullable=True)
    colis: int = Field(default=1, nullable=True)
    commentaire: str | None = Field(default=None, max_length=100, nullable=True)


"""Table representant les details des commandes."""
class DetailCommande(DetailCommandeBase, table=True):
    __tablename__ = "t_dticode"
    id: int | None = Field(default=None, primary_key=True)

"""Schema de validation pour la creation d'un detail de commande."""
class DetailCommandePost(DetailCommandeBase):
    pass

"""Schema de validation pour la mise a jour d'un detail de commande existant."""
class DetailCommandePatch(DetailCommandeBase):
    codcde: int | None = Field(default=None, foreign_key="t_entcde.codcde", index=True, nullable=True)
    qte: int = Field(default=1, nullable=True)
    colis: int = Field(default=1, nullable=True)
    commentaire: str | None = Field(default=None, max_length=100, nullable=True)
