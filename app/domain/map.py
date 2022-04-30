from dataclasses import dataclass
from typing import List

from app.domain.data import Size, Vector
from app.domain.entities.interfaces import Entity


@dataclass
class Map:
    """Класс карты."""

    size: Size
    entities: List[Entity]

    def get_entity(self, point: Vector) -> Entity:
        """Получить сущность по координатам."""
        for entity in self.entities:
            if (
                0 <= point.x - entity.location.x <= entity.size.width
                and 0 <= point.y - entity.location.y <= entity.size.height
            ):
                return entity

    def get_neighbour(self, entity: Entity) -> Entity:
        """Получить соседа по локации."""
        for neighbour in self.entities:
            if Entity.is_intersected(entity, neighbour):
                return neighbour

    def add_entity(self, entity: Entity) -> None:
        """Добавить сущность на карту."""
        # TODO проверка на возможность размещения сущности
        self.entities.append(entity)
