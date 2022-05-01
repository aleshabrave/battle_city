from dataclasses import dataclass
from typing import List

from app.domain.data import Size, Vector
from app.domain.entities.interfaces import Entity

CELL_SIZE = 10


@dataclass
class Map:
    """Класс карты."""

    _size: Size
    _entities: List[Entity]

    def get_entity(self, point: Vector) -> Entity:
        """Получить сущность по координатам."""

        for entity in self._entities:
            if (
                0 <= point.x - entity.location.x <= entity.size.width
                and 0 <= point.y - entity.location.y <= entity.size.height
            ):
                return entity

    def get_neighbour(self, entity: Entity) -> Entity:
        """Получить соседа по локации."""

        for neighbour in self._entities:
            if Entity.is_intersected(entity, neighbour):
                return neighbour

    def check_out_of_bounds(self, entity: Entity) -> bool:
        """Проверить выход сущности за пределы карты."""

        return (
            entity.location.x < 0
            or entity.location.x + entity.size.width >= self._size.width
            or entity.location.y < 0
            or entity.location.y + entity.size.height >= self._size.height
        )

    def add_entity(self, entity: Entity) -> None:
        """Добавить сущность."""

        self._entities.append(entity)

    def remove_entity(self, entity: Entity) -> None:
        """Удалить сущность."""

        self._entities.remove(entity)
