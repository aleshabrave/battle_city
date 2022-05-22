from typing import Optional

from app.db.storage import GameStorage
from app.domain.game import Game
from app.domain.level import Level
from app.levels import parser
from dataclasses import dataclass


@dataclass
class GameGenerator:
    """Генератор игры."""

    username: str
    storage: GameStorage
    game: Game = None

    def safe(self) -> None:
        """Сохранить игру."""
        self.storage.put(self.username, self.game)

    def load(self) -> Optional[Game]:
        """Загрузить игру."""
        return self.storage.get(self.username)

    @staticmethod
    def generate() -> Game:
        levels = []
        for i in range(3):
            levels.append(Level(parser.parse_map(f"maps/level_{i}.txt")))

        return Game(levels)
