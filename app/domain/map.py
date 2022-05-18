from dataclasses import dataclass

from app.domain.data import Size, Vector
from app.domain.data.params import are_intersected
from app.domain.entities.interfaces import Entity

CELL_SIZE = 8


@dataclass
class Map:
    """Класс карты."""

    size: Size
    _entities: dict[str, set[Entity]]

    def get_entities(self) -> set[Entity]:
        """Получить все сущности."""
        entities = set()
        for value in self._entities.values():
            entities |= value
        return entities

    def get_entities_by_name(self, name: str) -> set[Entity]:
        """Получить сущность по имени."""
        entities = self._entities.get(name, None)
        if entities is not None:
            return entities.copy()

    def get_entities_by_location(self, point: Vector, size: Size) -> set[Entity]:
        """Получить сущность по координатам."""
        entities = set()
        for entity in self.get_entities():
            if are_intersected(
                source=(point, size), other=(entity.location, entity.size)
            ):
                entities.add(entity)
        if len(entities) != 0:
            return entities

    def get_neighbours(self, entity: Entity) -> set[Entity]:
        """Получить соседа по локации."""
        entities = set()
        for neighbour in self.get_entities():
            if id(entity) != id(neighbour) and are_intersected(
                source=(entity.location, entity.size),
                other=(neighbour.location, neighbour.size),
            ):
                entities.add(neighbour)
        if len(entities) != 0:
            return entities

    def check_out_of_bounds(self, location: Vector, size: Size) -> bool:
        """Проверить выход сущности за пределы карты."""
        return (
            location.x < 0
            or location.x + size.width > self.size.width
            or location.y < 0
            or location.y + size.height > self.size.height
        )

    def add_entity(self, entity: Entity) -> None:
        """Добавить сущность."""
        if entity.name not in self._entities:
            self._entities[entity.name] = set()
        self._entities[entity.name].add(entity)

    def remove_entity(self, entity: Entity) -> None:
        """Удалить сущность."""
        if entity.name in self._entities:
            self._entities[entity.name].remove(entity)
            if len(self._entities[entity.name]) == 0:
                self._entities.pop(entity.name)
