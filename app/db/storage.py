from typing import Optional

import peewee

from app.db.models import GameModel, postgr_db
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
    def put(username: str, backup: Game) -> None:
        """Положить игру."""
        try:
            with postgr_db.atomic():
                GameModel.create(username=username, backup=backup)
        except peewee.IntegrityError:
            query = GameModel.update(backup=backup).where(
                GameModel.username == username
            )
            query.execute()
