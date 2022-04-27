from enum import Enum, unique


@unique
class GameState(Enum):
    """Состояние игры."""

    FINISHED = 1
    PLAY = 2
    PAUSE = 3


@unique
class GameResult(Enum):
    """Результаты игры."""
    WIN = 1
    LOSE = 2
    UNDEFINED = 3
