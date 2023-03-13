from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import PlayerCreate, PlayerModel
from models import GameCreate, GameModel
from tables_models import Player, Game

router_games = APIRouter(prefix='/game')
router_players = APIRouter(prefix='/player')


# players
@router_players.post('/', response_model=PlayerModel)
async def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    db_player = Player(name=player.name, surname=player.surname)
    if not(db_player.check_name_surname()):
        raise HTTPException(status_code=422, detail='Некорректное имя или фамилия')
    db_player.capitalize_name_surname()
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

@router_players.get('/{player_id}', response_model=PlayerModel)
def read_player(player_id: int, db: Session = Depends(get_db)):
    db_player = db.query(Player).filter(Player.id == player_id).first()
    if db_player is None:
        raise HTTPException(status_code=404, detail='Игрок не найден')
    return db_player


@router_players.delete('/{player_id}')
def delete_player(player_id: int, db: Session = Depends(get_db)):
    db_player = db.query(Player).filter(Player.id == player_id).first()
    if db_player is None:
        raise HTTPException(status_code=404, detail='Игрок не найден')
    db.delete(db_player)
    db.commit()
    return {"detail": f"Игрок с id {player_id} был удален"}


# games
@router_games.post('/', response_model=GameModel)
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    pass

@router_games.get('/{game_id}', response_model=GameModel)
def read_game(game_id: int, db: Session = Depends(get_db)):
    pass


@router_games.delete('/{game_id}')
def delete_game(game_id: int, db: Session = Depends(get_db)):
    pass
