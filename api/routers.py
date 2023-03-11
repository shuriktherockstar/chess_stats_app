from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Game, GameCreate, GameDelete
from models import Player, PlayerCreate, PlayerDelete

router_games = APIRouter(prefix='/game')
router_players = APIRouter(prefix='/player')

@router_games.post('/', response_model=GameCreate)
def create_player(game: GameCreate, db: Session = Depends(get_db)):
    pass

@router_games.get('/', response_model=Game)
def read_player():
    pass

@router_games.delete('/', response_model=GameDelete)
def delete_player():
    pass