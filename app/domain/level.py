from dataclasses import dataclass

from app.domain.data.enums import LevelResult
from app.domain.map import Map


@dataclass
class Level:
    """Класс уровня."""

    map_: Map
    state: LevelResult = LevelResult.UNDEFINED
