from sqlmodel import SQLModel, Field
from typing import Optional 


class ClientBase(SQLModel):
    """Schema de base representant les clients de la fidelisation de la fromagerie."""
    genrecli: Optional[str] | None = Field(default=None, max_length=8, nullable=False)
    nomcli: Optional[str] = Field(default=None, max_length=40, index=False)
    prenomcli: Optional[str] = Field(default=None, max_length=30)
    adresse1cli: Optional[str] = Field(default=None, max_length=50, nullable=True)
    adresse2cli: Optional[str] = Field(default=None, max_length=50, nullable=True)
    adresse3cli: Optional[str] = Field(default=None, max_length=50, nullable=True)
    villecli_id: Optional[int] = Field(default=None, foreign_key="t_communes.id", nullable=True)
    telcli: Optional[str] = Field(default=None, max_length=10, nullable=True)
    emailcli: Optional[str] = Field(default=None, max_length=255, nullable=True)
    portcli: Optional[str] = Field(default=None, max_length=10, nullable=True)
    newsletter: Optional[int] = Field(default=None, nullable=True)


class Client(ClientBase, table=True):
    codcli: Optional[int] = Field(default=None, primary_key=True)


class ClientPost(ClientBase):
    """Schema de validation pour la creation d'un nouveau client."""
    pass


class ClientPatch(ClientBase):
    """Schema de validation pour la mise a jour d'un client existant."""
    nomcli: Optional[str] = Field(default=None, max_length=40, index=True, nullable=True)
    prenomcli: Optional[str] = Field(default=None, max_length=30, nullable=True)