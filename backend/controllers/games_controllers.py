# controllers/games_controllers.py
from fastapi import APIRouter
from backend.models.games import GameInDB

router = APIRouter()


@router.post('/games', response_model=GameInDB)
def create_game():
    pass


@router.get('/games/{game_id}', response_model=GameInDB)
def read_game():
    pass


@router.put('/games/{player_id}', response_model=GameInDB)
def update_game():
    pass


@router.delete('/games/{player_id}', response_model=GameInDB)
def delete_game():
    pass
