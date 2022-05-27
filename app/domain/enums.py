from enum import Enum, unique
from math import pi


@unique
class GameState(str, Enum):
    """Состояние игры."""

    FINISHED = "Finished"
    PLAY = "Play"


@unique
class LevelResult(str, Enum):
    """Результат уровня."""

    WIN = "Win"
    LOSE = "Lose"
    UNDEFINED = "Undefined"


@unique
class Direction(Enum):
    """Направления движения в виде угла в радианах"""

    UP = pi / 2
    DOWN = -pi / 2
    LEFT = pi
    RIGHT = 0
