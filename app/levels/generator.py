import os
from typing import Optional

from app.db.storage import GameStorage
from app.domain import Game, Level
from app.levels import parser

_PATH = "./app/levels/maps/"


class GameGenerator:
    """Генератор игры."""

    @staticmethod
    def save(username: str, game: Game) -> None:
        """Сохранить игру."""
        GameStorage.put(username, game)

    @staticmethod
    def load(username: str) -> Optional[Game]:
        """Загрузить игру."""
        return GameStorage.get(username)

    @staticmethod
    def generate() -> Game:
        """Сгенерировать игру."""
        return Game(
            [
                Level(parser.parse_map(filename=_PATH + filename))
                for filename in sorted(os.listdir(f"{_PATH}"))
            ]
        )
