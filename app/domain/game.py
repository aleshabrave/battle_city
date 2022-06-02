from dataclasses import dataclass

from app.domain.enums import GameState
from app.domain.level import Level


@dataclass
class Game:
    """Класс игры."""

    _levels: list[Level]
    _idx: int = -1
    state: GameState = GameState.PLAY

    def __iter__(self):
        return iter(self._levels)

    def __next__(self):
        if self._idx + 1 < len(self._levels):
            self._idx += 1
            return self._levels[self._idx]
        else:
            raise StopIteration("Levels are over.")

    def get_current_level(self) -> Level:
        """Получить текущий уровень."""
        return self._levels[self._idx]
