# commande.py
from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class CommandeBase(SQLModel):
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
    __tablename__ = "t_entcde"
    codcde: Optional[int] = Field(default=None, primary_key=True)

    model_config = {
        "from_attributes": True
    }

class CommandePost(CommandeBase):
    pass

class CommandePatch(CommandeBase):
    pass
