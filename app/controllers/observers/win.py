from dataclasses import dataclass
from typing import TYPE_CHECKING

from app.domain.enums import LevelResult
from app.domain.interfaces import Observer, Living

if TYPE_CHECKING:
    from app.controllers.game_controller import GameController


@dataclass
class WinObserver(Observer):
    """Класс наблюдателя за победой."""

    _enemies: list[Living]
    _game_controller: "GameController"

    def handle_event(self) -> None:
        """Обработать событие."""
        available_enemies: list[Living] = []

        for enemy in self._enemies:
            if enemy.is_available():
                available_enemies.append(enemy)
            else:
                enemy.remove_observer(self)

        self._enemies = available_enemies
        if self._enemies:
            return

        self._game_controller.game.get_current_level().state = LevelResult.WIN
        self._game_controller.update_controller()
