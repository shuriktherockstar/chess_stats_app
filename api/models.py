# pydantic-models

from pydantic import BaseModel

# players

class PlayerBase(BaseModel):
    name: str
    surname: str


class PlayerCreate(PlayerBase):
    pass


class PlayerModel(PlayerBase):
    id: int

    class Config:
        orm_mode = True


# games

class GameBase(BaseModel):
    player1_id: int
    player2_id: int
    result: str


class GameCreate(GameBase):
    pass


class GameModel(GameBase):
    id: int

    class Config:
        orm_mode = True
