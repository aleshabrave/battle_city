from dataclasses import dataclass

from app.domain.interfaces import Movable
from app.domain.map import Map


@dataclass
class MapController:
    """Класс контроллера Map."""

    _map: Map

    def update_map(self) -> None:
        """Обновить состояние карты."""
        for entity in self._map.entities:
            if isinstance(entity, Movable):
                entity.update_location(self._map)
