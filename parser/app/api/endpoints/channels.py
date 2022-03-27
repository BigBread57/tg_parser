from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.db import base_class
from app.db.session import engine

base_class.Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get('/', response_model=List[schemas.Channel], tags=['channels'])
def read_channels(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve items.
    """

    channels = crud.channel.get_multi(db, skip=skip, limit=limit)
    return channels


@router.post('/get-info', response_model=List[schemas.Channel], tags=['channels'])
def read_channels(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve items.
    """

    channels = crud.channel.get_multi(db, skip=skip, limit=limit)
    return channels
