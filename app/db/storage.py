from typing import Optional

from app.db.models import GameModel
from app.domain.game import Game


class GameStorage:
    """Storage for GameModel."""

    @staticmethod
    def get(username: str) -> Optional[Game]:
        """Get game."""
        game = GameModel.get_or_none(GameModel.username == username)

        if game is not None:
            return game.backup

    @staticmethod
    def put(username: str, backup: Game) -> None:
        """Put game."""
        game, _ = GameModel.get_or_create(username=username)
        game.backup = backup
        game.save()
