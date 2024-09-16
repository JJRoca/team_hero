from fastapi import APIRouter, HTTPException
from app.utils.pagination import MetaData, ResponseModel
from app.core.dependencies import sessionDep
from app.models.team import Message, TeamCreate, TeamPublic,TeamUpdate
from app.services import team_service
from app.models.models_common import TeamPublicWithHeroes
import uuid

router=APIRouter()

@router.post("/team/", tags= ["Team"], response_model=TeamPublic)
def create_team(*, session: sessionDep, team: TeamCreate):
    """
    Create a Team with all the information:

    - **id**: Uniquer identifier for each Team, generated automatically (auto-increment)
    - **name**: Uniquer name for each Team
    - **headquarters**: headquarters for each team
    """
    return team_service.create_team(session= session, team= team)


@router.get("/teams/", tags= ["Team"],response_model=ResponseModel[TeamPublic])
def get_all_teams(*, session: sessionDep, skip:int=0, limit:int=10):
    #calculate the current page
    page=(skip//limit)+1
    #fetch the teams and total numbers of teams from the service
    teams= team_service.get_all_teams(session=session, skip=skip, limit=limit)

    #calculate the total number of pages
    total_pages=(teams["total_items"]//limit)+(1 if teams["total_items"]%limit>0 else 0)
    
    #calculate the previous and next pages
    previous_page= page - 1 if page>1 else None
    next_page= page + 1 if page < total_pages else None
    
    #avoid "skip" being greater than "total_items"
    if skip >= teams["total_items"]:
        raise HTTPException(status_code=400, detail="skip value is greater than total items.")
    
    return ResponseModel(
        data=teams["teams"],
        meta=MetaData(
            total_items=teams["total_items"],
            current_page=page,
            per_page=limit,
            total_page=total_pages,
            previous_page=previous_page,
            next_page=next_page
        )
    )


@router.get("/team/{team_id}", tags= ["Team"],response_model=TeamPublicWithHeroes)
def get_team_by_id(*, session: sessionDep, team_id: uuid.UUID):
    team= team_service.get_team_by_id(session= session, team_id= team_id)
    return team
@router.patch("/team/{team_id}",tags= ["Team"], response_model=TeamPublic)
def update_team(*, session: sessionDep, team_id: uuid.UUID, team: TeamUpdate):
    team= team_service.update_team(session=session, team_id=team_id, team= team)
    return team


@router.delete("/team/{team_id}", tags= ["Team"],response_model=Message)
def delete_team(*, session: sessionDep, team_id: uuid.UUID):
    team_service.delete_team(session=session, team_id= team_id)
    return Message(message= "Team deleted successfully")