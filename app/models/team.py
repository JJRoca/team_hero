from sqlmodel import SQLModel,Field,Relationship
import uuid
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .hero import Hero

class TeamBase(SQLModel):
    name: str = Field(index= True, unique= True)
    headquarters:str

class Team(TeamBase, table= True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    heroes: list["Hero"] =  Relationship(back_populates= "team")

class TeamCreate(TeamBase):
    pass

class TeamPublic(TeamBase):
    id: uuid.UUID

class TeamUpdate(SQLModel):
    #id: uuid.UUID|None= None
    name: str|None= None
    headquarters: str|None= None

class Message(SQLModel):
    message: str
