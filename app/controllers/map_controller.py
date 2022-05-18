from dataclasses import dataclass

from app.domain.entities.interfaces import MovableEntity
from app.domain.map import Map


@dataclass
class MapController:
    """Класс контроллера для Map."""

    _map: Map

    def update_map(self) -> Map:
        """Обновить карту."""
        self._move_entities()

        return self._map

    def _move_entities(self) -> None:
        """Подвинуть moveable entities."""
        for entity in self._map.get_entities():
            if isinstance(entity, MovableEntity):
                entity.update_location(self._map)
