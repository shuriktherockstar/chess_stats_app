# controllers/players_controllers.py
from fastapi import APIRouter
from backend.models.players import PlayerInDB

router = APIRouter()


@router.post('/players', response_model=PlayerInDB)
def create_player():
    pass


@router.get('/players/{player_id}', response_model=PlayerInDB)
def read_player():
    pass


@router.put('/players/{player_id}', response_model=PlayerInDB)
def update_player():
    pass


@router.delete('/players/{player_id}', response_model=PlayerInDB)
def delete_player():
    pass
