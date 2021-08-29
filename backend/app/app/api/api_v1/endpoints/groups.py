from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app import crud, models, schemas

""" Endpoints for groups.

Create, delete, update group.
Send messages, get users in group, ping, load emotes, upload emote.

TODO: Partition groups by server 
https://docs.sqlalchemy.org/en/14/orm/persistence_techniques.html#partitioning-strategies-e-g-multiple-database-backends-per-session

TODO: Add replication later
"""

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users

