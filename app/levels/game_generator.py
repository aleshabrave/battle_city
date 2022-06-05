import os
from typing import Optional

from app.db.storage import GameStorage
from app.domain import Game, Level
from app.levels import parser
from app.levels.tank_generator import TankFabric

_PATH = "./app/levels/maps/"


class GameGenerator:
    """Game generator."""

    @staticmethod
    def save(username: str, game: Game) -> None:
        """Save game."""
        GameStorage.put(username, game)

    @staticmethod
    def load(username: str) -> Optional[Game]:
        """Load game."""
        return GameStorage.get(username)

    @staticmethod
    def generate(player_fabric: TankFabric) -> Game:
        """Generate new game."""
        return Game(
            [
                Level(
                    parser.get_map(
                        filename=_PATH + filename, player_fabric=player_fabric
                    )
                )
                for filename in sorted(os.listdir(f"{_PATH}"))
            ]
        )
