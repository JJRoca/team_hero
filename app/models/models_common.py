from .team import TeamPublic
from .hero import HeroPublic
from typing import Optional
class heroPublicWithTeam(HeroPublic):
    team: Optional["TeamPublic"]=None
    #pass


class TeamPublicWithHeroes(TeamPublic):
    heroes: list["HeroPublic"]= []