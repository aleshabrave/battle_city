from dataclasses import dataclass

from app.domain import Game, Level
from app.domain.enums import LevelState
from app.domain.interfaces import Living, Observer


@dataclass
class WinObserver(Observer):
    """Класс наблюдателя за победой."""

    _enemies: list[Living]
    _level: Level
    _game: Game

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

        self._level.state = LevelState.WIN
