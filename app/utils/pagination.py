from typing import Generic, TypeVar
from sqlmodel import SQLModel
from pydantic import BaseModel

T= TypeVar("T", bound=SQLModel)
class MetaData(BaseModel):
    total_items: int
    current_page: int
    per_page: int
    total_page: int
    previous_page: int|None
    next_page: int|None

class ResponseModel(BaseModel, Generic[T]):
    data: list[T]
    meta: MetaData
