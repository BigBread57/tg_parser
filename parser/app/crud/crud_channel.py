from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase, ModelType
from app.models.channel import Channel
from app.schemas.channel import ChannelCreate, ChannelUpdate


class CRUDChannel(CRUDBase[Channel, ChannelCreate, ChannelUpdate]):
    pass


channel = CRUDChannel(Channel)
