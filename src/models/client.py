from sqlmodel import SQLModel, Field

"""Schema de base representant les clients de la fidelisation de la fromagerie."""
class ClientBase(SQLModel):
    genrecli: str | None = Field(default=None, max_length=8, nullable=False)
    nomcli: str = Field(default=None, max_length=40, index=False)
    prenomcli: str = Field(default=None, max_length=30)
    adresse1cli: str | None = Field(default=None, max_length=50, nullable=True)
    adresse2cli: str | None = Field(default=None, max_length=50, nullable=True)
    adresse3cli: str | None = Field(default=None, max_length=50, nullable=True)
    villecli_id: int | None = Field(default=None,  nullable=True)#foreign_key="t_communes.id",
    telcli: str | None = Field(default=None, max_length=10, nullable=True)
    emailcli: str | None = Field(default=None, max_length=255, nullable=True)
    portcli: str | None = Field(default=None, max_length=10, nullable=True)
    newsletter: int | None = Field(default=None, nullable=True)

"""Table representant les clients de la fidelisation de la fromagerie."""
class Client(ClientBase, table=True):
    __tablename__ = "t_client"
    codcli: int | None = Field(default=None, primary_key=True)

"""Schema de validation pour la creation d'un nouveau client."""
class ClientPost(ClientBase):
    pass

"""Schema de validation pour la mise a jour d'un client existant."""
class ClientPatch(ClientBase):
    nomcli: str | None = Field(default=None, max_length=40, index=True, nullable=True)
    prenomcli: str | None = Field(default=None, max_length=30, nullable=True)