from dataclasses import dataclass

from app.domain.enums import GameState
from app.domain.level import Level


@dataclass
class Game:
    """Class for game."""

    _levels: list[Level]
    _idx: int = -1
    state: GameState = GameState.PLAY

    def __iter__(self):
        return iter(self._levels)
