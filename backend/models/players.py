# models/players.py
from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    surname: str


class PlayerCreate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True
