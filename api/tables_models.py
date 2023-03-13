from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# класс "Игрок"
class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    surname = Column(String(50))

    def check_name_surname(self) -> bool:
        permitted_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\'- "
        if set(self.name).issubset(permitted_chars) and set(self.surname).issubset(permitted_chars):
            return True
        else:
            return False

    def capitalize_name_surname(self):
        special_chars = [' ', '-', '\'']
        for char in special_chars:
            char_parts = [part.capitalize() for part in self.name.split(char)]
            self.name = char.join(char_parts)

        for char in special_chars:
            char_parts = [part.capitalize() for part in self.surname.split(char)]
            self.surname = char.join(char_parts)


# класс "Игра"
class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, index=True)
    player1_id = Column(Integer, ForeignKey('players.id'))
    player2_id = Column(Integer, ForeignKey('players.id'))
    winner_id = Column(Integer, ForeignKey('players.id'))

    player1 = relationship('Player', foreign_keys=[player1_id])
    player2 = relationship('Player', foreign_keys=[player2_id])
    winner = relationship('Player', foreign_keys=[winner_id])
