from typing import Optional

from pydantic import BaseModel


# Общие свойства
class MessageBase(BaseModel):
    text: Optional[str] = None
    image: Optional[str] = None
    url: Optional[str] = None
    document: Optional[str] = None
    video: Optional[str] = None


# Свойства, которые нужно получить при создании элемента
class MessageCreate(MessageBase):
    text: Optional[str] = None
    image: Optional[str] = None
    url: Optional[str] = None
    document: Optional[str] = None
    video: Optional[str] = None


# Свойства, которые нужно получить при обновлении элемента
class MessageUpdate(MessageBase):
    text: Optional[str] = None
    image: Optional[str] = None
    url: Optional[str] = None
    document: Optional[str] = None
    video: Optional[str] = None


# Свойства, общие для моделей, хранящиеся в БД
class MessageInDBBase(MessageBase):
    id: int
    channel_id: int

    class Config:
        orm_mode = True


# Свойства, которые нужно вернуть клиенту
class Message(MessageInDBBase):
    pass


# Свойства свойств, хранящиеся в БД
class MessageInDB(MessageInDBBase):
    pass
