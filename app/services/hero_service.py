from fastapi import HTTPException
from sqlmodel import Session, select,func
from app.core.security import hashPassword
from app.models.hero import Hero, HeroCreate, HeroUpdate
from app.services.team_service import get_team_by_id

from app.models.team import Team
def get_hero_by_id(*, session: Session, id: int):
    db_hero= session.get(Hero, id)
    return db_hero


def get_all_heroes(*, session: Session, skip: int, limit: int):
    count_statement= select(func.count()).select_from(Hero)
    count= session.exec(count_statement).one()
    db_heroes= session.exec(select(Hero).where(Hero.is_active==True).offset(skip).limit(limit)).all()
    return {"heroes":db_heroes,"total_items":count}

def create_hero(*, session: Session,hero: HeroCreate):
    get_team_by_id(session=session,team_id=hero.team_id)
    db_hero=Hero.model_validate(
        hero,update={"secret_name":hashPassword(hero.secret_name)})
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

def delete_hero(*, session:Session, hero_id: int):
    db_hero= session.get(Hero,hero_id)
    if not db_hero:
        raise HTTPException(status_code=404,detail="Hero not found")
    #logically deletes a user from the database by updating the 'is_active' field instead of physically removing the record
    db_hero.is_active=False
    session.add(db_hero)
    session.commit()
    #session.refresh(db_hero)
    return db_hero

def update_hero(*,session:Session, hero_id:int, hero:HeroUpdate):
    db_hero= session.get(Hero, hero_id)
    if not db_hero:
        raise HTTPException(status_code=404,detail="Hero not found")
    if not db_hero.is_active:
        raise HTTPException(status_code=404, detail="Cannot update a logically deleted hero")
    
    hero_data=hero.model_dump(exclude_unset=True)
    db_hero.sqlmodel_update(hero_data)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero
