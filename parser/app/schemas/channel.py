from typing import Optional

from pydantic import BaseModel


# Общие свойства
from app.schemas import Message


class ChannelBase(BaseModel):
    name: str | None = None


# Свойства, которые нужно получить при создании элемента
class ChannelCreate(ChannelBase):
    name: str | None = None


# Свойства, которые нужно получить при обновлении элемента
class ChannelUpdate(ChannelBase):
    name: str | None = None


# Свойства, общие для моделей, хранящиеся в БД
class ChannelInDBBase(ChannelBase):
    id: int
    messages: list[Message] = []

    class Config:
        orm_mode = True


# Свойства, которые нужно вернуть клиенту
class Channel(ChannelInDBBase):
    pass


# Свойства свойств, хранящиеся в БД
class ChannelInDB(ChannelInDBBase):
    pass
