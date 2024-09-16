from fastapi import APIRouter, HTTPException
from app.models.hero import HeroPublic,HeroCreate,Hero, HeroUpdate, Message
from app.models.models_common import heroPublicWithTeam
from app.core.dependencies import sessionDep
from app.core.security import hashPassword
from app.services import hero_service
from app.utils.pagination import MetaData, ResponseModel
router=APIRouter()

#Get user by id
@router.get("/hero/{hero_id}",tags=["Hero"],response_model=heroPublicWithTeam)
def get_hero_by_id(*, session: sessionDep, hero_id: int):
    result=hero_service.get_hero_by_id(session= session, id= hero_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result   
                     
#create hero 
@router.post("/heroes/",tags=["Hero"], response_model= HeroPublic, summary= "Create a Hero")
def create_hero(*, session: sessionDep, hero: HeroCreate):
    """
    Create a Hero with all the information:

    - **id**: Uniquer identifier for each Hero, generated automatically (auto-increment)
    - **age**: Optional 
    - **name**: Optional
    - **team_id**: Required, foreign key referencing the team 
    - **created_at**: The timestamp when the Hero is created (automatically generated).
    """
    return hero_service.create_hero(session=session, hero= hero)

#Get all heros
@router.get("/heroes",tags=["Hero"], response_model= ResponseModel[HeroPublic])
def get_all_heroes(*, session: sessionDep, skip:int= 0, limit:int= 5):
    page= (skip//limit)+1
    heroes= hero_service.get_all_heroes(session=session, skip=skip, limit=limit)
    total_pages=(heroes["total_items"]//limit)+(1 if heroes["total_items"]%limit>0 else 0)
    #calculate the previous and next pages
    previous_page= page - 1 if page>1 else None
    next_page= page + 1 if page < total_pages else None
    
    #avoid "skip" being greater than "total_items"
    if skip >= heroes["total_items"]:
        raise HTTPException(status_code=400, detail="skip value is greater than total items.")
    return ResponseModel(
        data=heroes["heroes"],
        meta=MetaData(
            total_items=heroes["total_items"],
            current_page=page,
            per_page=limit,
            total_page=total_pages,
            previous_page=previous_page,
            next_page=next_page
        )
    )

@router.delete("/hero/{team_id}",tags=["Hero"],response_model=Message)
def delete_hero(*, session: sessionDep, hero_id:int, hero: HeroUpdate):
    hero_service.delete_hero(session=session, hero_id=hero_id, hero=hero)
    return Message(
        message="Hero deleted successfully"
    )
@router.patch("/hero/{hero_id}",tags=["Hero"],response_model=HeroPublic)
def update_hero(*,session: sessionDep, hero_id:int, hero:HeroUpdate):
    return hero_service.update_hero(session=session, hero_id=hero_id,hero=hero)