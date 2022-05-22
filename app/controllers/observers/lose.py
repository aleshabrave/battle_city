from dataclasses import dataclass
from typing import TYPE_CHECKING

from app.domain.enums import LevelResult
from app.domain.interfaces import Observer, Living

if TYPE_CHECKING:
    from app.controllers.game_controller import GameController


@dataclass
class LoseObserver(Observer):
    """Класс наблюдателя за победой."""

    _entities: list[Living]
    _game_controller: "GameController"

    def handle_event(self) -> None:
        """Обработать событие."""

        for entity in self._entities:
            if not entity.is_available():
                self._clear()
                self._game_controller.game.get_current_level().state = LevelResult.LOSE
                return

    def _clear(self) -> None:
        for entity in self._entities:
            entity.remove_observer(self)
