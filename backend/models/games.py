# models/games.py
from pydantic import BaseModel


class GameBase(BaseModel):
    player1_id: int
    player2_id: int
    result: str


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int

    class Config:
        orm_mode = True
