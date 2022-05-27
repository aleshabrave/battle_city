from typing import Optional

from app.db.models import GameModel
from app.domain.game import Game


class GameStorage:
    """Класс для работы с GameModel."""

    @staticmethod
    def get(username: str) -> Optional[Game]:
        """Получить игру."""
        game = GameModel.get_or_none(GameModel.username == username)

        if game is not None:
            return game.backup

    @staticmethod
    def put(username: str, game: Game) -> None:
        """Положить игру."""
        GameModel.insert(username=username, backup=game)
