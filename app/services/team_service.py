from fastapi import HTTPException
from app.models.team import TeamCreate, Team, TeamUpdate
from sqlmodel import Session, select,func
from app.models.hero import Hero
import uuid
def create_team(*, session: Session , team: TeamCreate):
    db_team= Team.model_validate(team)
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    return db_team

def get_team_by_id(*, session: Session, team_id: uuid.UUID):
    db_team= session.get(Team, team_id)
    if not db_team:
         raise HTTPException(status_code=404, detail="Team id not found, please enter a valid team_id") 
    #Filter actives heroes
    statement = select(Hero).where(
        Hero.team_id == team_id,
        Hero.is_active == True
    )
    result = session.exec(statement)
    print("------------->",result)
    active_heroes = result.fetchall()
    # Puedes añadir los héroes activos a tu equipo si es necesario
    db_team.heroes = active_heroes

    return db_team

def get_all_teams(*, session: Session, skip: int, limit: int):
    #calculate the total number of teams (count) from the table Team
    count_statement=select(func.count()).select_from(Team)
    count = session.exec(count_statement).one()

    db_teams= session.exec(select(Team).offset(skip).limit(limit)).all()
    #teams= [team.model_dump() for team in db_teams]
    return {"teams":db_teams,"total_items":count}


def update_team(*, session: Session, team_id: uuid.UUID, team: TeamUpdate):

    db_team = session.get(Team,team_id)
    if not db_team:
            raise HTTPException(status_code=404, detail="Team not found")
    team_data=team.model_dump(exclude_unset=True)
    db_team.sqlmodel_update(team_data)
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    return db_team

def delete_team(*, session: Session, team_id: uuid.UUID):
    db_team= session.get(Team,team_id)
    if not db_team:
         raise HTTPException(status_code=404, detail="Team not found")
    session.delete(db_team)
    session.commit()
    return db_team