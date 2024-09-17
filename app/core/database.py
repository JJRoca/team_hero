#from models.hero import Hero
#from models.team import Team
import dotenv.variables
from sqlmodel import SQLModel, create_engine
import dotenv
import os
dotenv.load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")

engine= create_engine(DATABASE_URL,echo= True)

#print(DATABASE_URL)

def create_db_tables():
    SQLModel.metadata.create_all(engine)
