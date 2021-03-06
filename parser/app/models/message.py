from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .channel import Channel  # noqa: F401


class Message(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    image = Column(String, nullable=True)
    url = Column(String, nullable=True)
    document = Column(String, nullable=True)
    video = Column(String, nullable=True)
    channel_id = Column(Integer, ForeignKey('channel.id'))

    channel = relationship("Channel", back_populates="messages")
