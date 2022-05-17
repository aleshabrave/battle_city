from dataclasses import dataclass

from app.domain.data.enums import GameState
from app.domain.level import Level


@dataclass
class Game:
    """Класс игры."""

    _levels: list[Level]
    _current_level_index: int = 0
    state: GameState = GameState.PAUSE

    def get_current_level(self) -> Level:
        """Получить текущий уровень."""
        if self._current_level_index >= len(self._levels):
            raise IndexError("Levels are over.")
        return self._levels[self._current_level_index]

    def next_level(self) -> bool:
        """Перейти на следующий уровень."""
        if self._current_level_index + 1 >= len(self._levels):
            return False
        self._current_level_index += 1
        return True
