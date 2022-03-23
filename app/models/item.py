from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Channel(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Message(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    image = Column(String, nullable=True)
    url = Column(String, nullable=True)
    document = Column(String, nullable=True)
    video = Column(String, nullable=True)
    owner_id = Column(Integer)
    owner = relationship('Channel', back_populates='messages')
