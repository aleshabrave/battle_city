from dataclasses import dataclass
from typing import List

from app.domain.data import Size, Vector
from app.domain.entities.interfaces import Entity
from app.domain.entities.tank import Tank

CELL_SIZE = 10


@dataclass
class Map:
    """Класс карты."""

    size: Size
    entities: List[Entity]
    player: Tank

    def get_entity_by_name(self, name: str) -> List[Entity]:
        """Получить сущность по имени."""
        return [entity for entity in self.entities if entity.name == name]

    def get_entity_by_location(self, point: Vector) -> Entity:
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
            if id(entity) != id(neighbour) and Entity.are_intersected(
                entity, neighbour
            ):
                return neighbour

    def check_out_of_bounds(self, entity: Entity) -> bool:
        """Проверить выход сущности за пределы карты."""
        return (
            entity.location.x < 0
            or entity.location.x + entity.size.width >= self.size.width
            or entity.location.y < 0
            or entity.location.y + entity.size.height >= self.size.height
        )

    def add_entity(self, entity: Entity) -> None:
        """Добавить сущность."""
        self.entities.append(entity)

    def remove_entity(self, entity: Entity) -> None:
        """Удалить сущность."""
        self.entities.remove(entity)
