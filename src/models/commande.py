from sqlmodel import SQLModel, Field
from datetime import date

"""Schema de base representant les commandes passees par les clients."""
class CommandeBase(SQLModel):  # Schéma de validation
    datcde: date | None = Field(default=None, nullable=True)
    codcli: int | None = Field(default=None, foreign_key="t_client.codcli", nullable=True)
    timbrecli: float | None = Field(default=None, nullable=True)
    timbrecde: float | None = Field(default=None, nullable=True)
    nbcolis: int | None = Field(default=1, nullable=True)
    cheqcli: float | None = Field(default=None, nullable=True)
    idcondit: int | None = Field(default=0, nullable=True)
    cdeComt: str | None = Field(default=None, max_length=255, nullable=True)
    barchive: int | None = Field(default=0, nullable=True)
    bstock: int | None = Field(default=0, nullable=True)

"""Table representant les commandes passees par les clients."""
class Commande(SQLModel, table=True):
    __tablename__ = "t_entcde"
    codcde: int | None = Field(default=None, primary_key=True)

class CommandePost(CommandeBase):
    pass

class CommandePatch(CommandeBase):
    datcde: date | None = Field(default=None, nullable=True)
    codcli: int | None = Field(default=None, foreign_key="t_client.codcli", nullable=True)
    timbrecli: float | None = Field(default=None, nullable=True)
    timbrecde: float | None = Field(default=None, nullable=True)
    nbcolis: int | None = Field(default=1, nullable=True)
    cheqcli: float | None = Field(default=None, nullable=True)
    idcondit: int | None = Field(default=0, nullable=True)
    cdeComt: str | None = Field(default=None, max_length=255, nullable=True)
    barchive: int | None = Field(default=0, nullable=True)
    bstock: int | None = Field(default=0, nullable=True)