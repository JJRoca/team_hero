import uuid
from datetime import datetime
from sqlmodel import SQLModel,Field,Relationship
from typing import TYPE_CHECKING,Optional

if TYPE_CHECKING:
    from .team import Team

#share properties
class HeroBase(SQLModel):
    name: str= Field(index= True)
    age: int|None = Field(default= None, index= True)
    team_id: uuid.UUID|None = Field(default=None, foreign_key="team.id")

#Database model 
class Hero(HeroBase, table=True):
    id: int|None= Field(default=None, primary_key=True)
    secret_name: str
    is_active: bool= Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    team: Optional["Team"] = Relationship(back_populates="heroes")

class HeroCreate(HeroBase):
    secret_name: str

class HeroPublic(HeroBase):
    id: int
    created_at: datetime|None=None

class HeroUpdate(SQLModel):
    name: str|None=None
    age: int|None =None

class Message(SQLModel):
    message: str
    
