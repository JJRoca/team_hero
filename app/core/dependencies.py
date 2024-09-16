from typing import Annotated
from fastapi import Header,HTTPException
from typing import Annotated
from sqlmodel import Session
from collections.abc import Generator
from fastapi import Depends
from app.core.database import engine
def get_session()->Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        
sessionDep=Annotated[Session, Depends(get_session)]


# async def get_token_header(x_token: Annotated[str, Header()]):
#     if x_token!="fake-super-secret-token":
#         raise HTTPException(status_code=404, detail="X-Token header invalid")

# async def get_query_token(token: str):
#     if token != "jessica":
#         raise HTTPException(status_code=400, detail="No Jessica token provided")
    

    