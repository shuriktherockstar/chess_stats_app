from pydantic import BaseModel

# games

class GameBase(BaseModel):
    player1_id: int
    player2_id: int
    result: str


class GameCreate(GameBase):
    pass


class GameDelete(GameBase):
    id: int


class Game(GameBase):
    id: int

    class Config:
        orm_mode = True


# players

class PlayerBase(BaseModel):
    name: str
    surname: str


class PlayerCreate(PlayerBase):
    pass


class PlayerDelete(PlayerBase):
    id: int


class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True
