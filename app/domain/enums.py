from enum import Enum, unique
from math import pi


@unique
class GameState(Enum):
    """Состояние игры."""

    FINISHED = 1
    PLAY = 2


@unique
class LevelResult(Enum):
    """Результат уровня."""

    WIN = 1
    LOSE = 2
    UNDEFINED = 3


@unique
class Direction(Enum):
    """Направления движения в виде угла в радианах"""

    UP = pi / 2
    DOWN = -pi / 2
    LEFT = pi
    RIGHT = 0