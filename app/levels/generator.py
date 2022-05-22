import os
from dataclasses import dataclass
from typing import Optional

from app.db.storage import GameStorage
from app.domain import Game, Level
from app.levels import parser


@dataclass
class GameGenerator:
    """Генератор игры."""

    username: str

    def save(self, game: Game) -> None:
        """Сохранить игру."""
        GameStorage.put(self.username, game)

    def load(self) -> Optional[Game]:
        """Загрузить игру."""
        return GameStorage.get(self.username)

    @staticmethod
    def generate() -> Game:
        """Сгенерировать игру."""
        levels = []

        for i in range(len(os.listdir("./app/levels/maps/"))):
            level = Level(parser.parse_map(f"./app/levels/maps/map_{i}.txt"))
            levels.append(level)

        return Game(levels)
