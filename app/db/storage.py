from typing import Optional

from app.db.models import GameModel
from app.domain.game import Game


class GameStorage:
    @staticmethod
    def get(username: str) -> Optional[Game]:
        game = GameModel.get_or_none(GameModel.username == username)

        if game is not None:
            return game.backup

    @staticmethod
    def put(username: str, game: Game) -> None:
        GameModel.create(username=username, backup=game)
