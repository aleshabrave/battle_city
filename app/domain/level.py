from dataclasses import dataclass

from app.domain.enums import LevelState
from app.domain.map import Map


@dataclass
class Level:
    """Class for level."""

    map_: Map
    state: LevelState = LevelState.UNDEFINED
