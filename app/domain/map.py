from dataclasses import dataclass

from app.domain.interfaces import Entity
from app.domain.utils import Methods, Size, Vector


@dataclass
class Map:
    """Класс карты."""

    size: Size
    entities: list[Entity] = None

    def __post_init__(self):
        if self.entities is None:
            self.entities = []

    def get_enemies(self) -> list[Entity]:
        """Get all enemies."""
        return [
            entity
            for entity in self.entities
            if "enemy" in entity.name and "tank" in entity.name
        ]

    def get_player(self) -> Entity:
        """Get player."""
        return [entity for entity in self.entities if "player" in entity.name][0]

    def get_entities_by_name(self, name: str) -> list[Entity]:
        """Получить сущности по имени."""
        return [entity for entity in self.entities if entity.name == name]

    def get_entities_by_location(self, position: Vector, size: Size) -> list[Entity]:
        """Получить сущность по координатам."""
        return [
            entity
            for entity in self.entities
            if Methods.are_intersected(
                source=(entity.position, entity.size), other=(position, size)
            )
        ]

    def check_out_of_bounds(self, position: Vector, size: Size) -> bool:
        """Проверить выход за пределы карты."""
        return (
            position.x < 0
            or position.x + size.width > self.size.width
            or position.y < 0
            or position.y + size.height > self.size.height
        )

    def add_entity(self, entity: Entity) -> None:
        """Добавить сущность."""
        self.entities.append(entity)

    def remove_entity(self, entity: Entity) -> None:
        """Удалить сущность."""
        self.entities.remove(entity)
