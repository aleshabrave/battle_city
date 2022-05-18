from dataclasses import dataclass
from typing import TYPE_CHECKING

from app.domain.data import LevelResult
from app.domain.entities.interfaces import Living
from app.domain.interfaces import Observer

if TYPE_CHECKING:
    from app.controllers.game_controller import GameController


@dataclass
class WinObserver(Observer):
    """Класс наблюдателя за поражением."""

    _enemies: set[Living]
    _game_controller: "GameController"

    def handle_event(self) -> None:
        """Обработать событие."""
        some_enemies = False

        for enemy in self._enemies:
            if not enemy.is_available():
                some_enemies = True

        if some_enemies:
            return

        self._game_controller.game.get_current_level().state = LevelResult.WIN
        self._game_controller.update_controller()
