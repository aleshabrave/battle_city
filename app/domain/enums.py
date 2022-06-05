from enum import Enum, unique
from math import pi


@unique
class GameState(str, Enum):
    """Game state."""

    FINISHED = "Finished"
    PLAY = "Play"


@unique
class LevelState(str, Enum):
    """Level state."""

    WIN = "Win"
    LOSE = "Lose"
    UNDEFINED = "Undefined"


@unique
class Direction(Enum):
    """Direction of travel."""

    UP = pi / 2
    DOWN = -pi / 2
    LEFT = pi
    RIGHT = 0
