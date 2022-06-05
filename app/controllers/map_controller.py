from dataclasses import dataclass
from typing import TYPE_CHECKING

from app.domain.interfaces import Movable

if TYPE_CHECKING:
    from app.domain.map import Map


@dataclass
class MapController:
    """Controller for map."""

    map_: "Map"

    def update_map(self) -> None:
        """Update map's state."""
        for entity in list(reversed(self.map_.entities)):
            if isinstance(entity, Movable):
                entity.update_location(self.map_)
