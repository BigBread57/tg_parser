from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from parser.crud.base import CRUDBase
from parser.models.channel import Channel
from parser.schemas.channel import ChannelCreate, ChannelUpdate


class CRUDItem(CRUDBase[Channel, ChannelCreate, ChannelUpdate]):
    def create(
        self, db: Session, *, obj_in: ChannelCreate
    ) -> Channel:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get (
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Channel]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )


item = CRUDItem(Channel)
