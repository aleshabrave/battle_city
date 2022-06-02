from dataclasses import dataclass
from typing import TYPE_CHECKING

from app.domain.interfaces import Movable

if TYPE_CHECKING:
    from app.domain.map import Map


@dataclass
class MapController:
    """Класс контроллера Map."""

    map_: "Map"

    def update_map(self) -> None:
        """Обновить состояние карты."""
        for entity in self.map_.entities:
            if isinstance(entity, Movable):
                entity.update_location(self.map_)
