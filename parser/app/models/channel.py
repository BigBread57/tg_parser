from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class Channel(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
