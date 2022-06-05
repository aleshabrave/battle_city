from dataclasses import dataclass

from app.domain.exceptions import MapException
from app.domain.interfaces import Entity
from app.domain.utils import Methods, Size, Vector


@dataclass
class Map:
    """Class for map."""

    size: Size
    entities: list[Entity] = None

    def __post_init__(self):
        if self.entities is None:
            self.entities = []

    def get_enemy_tanks(self) -> list[Entity]:
        """Get all enemy tanks."""
        return [
            entity
            for entity in self.entities
            if "enemy" in entity.name and "tank" in entity.name
        ]

    def get_player_tank(self) -> Entity:
        """Get player tank."""
        players = [
            entity
            for entity in self.entities
            if "player" in entity.name and "tank" in entity.name
        ]
        if len(players) == 0:
            raise MapException("No player.")
        if len(players) > 1:
            raise MapException("Too many players, but should be only one.")
        return players[0]

    def get_entities_by_name(self, name: str) -> list[Entity]:
        """Get entities by name."""
        return [entity for entity in self.entities if entity.name == name]

    def get_entities_by_location(self, position: Vector, size: Size) -> list[Entity]:
        """Get entities by location."""
        return [
            entity
            for entity in self.entities
            if Methods.are_intersected(
                source=(entity.position, entity.size), other=(position, size)
            )
        ]

    def check_out_of_bounds(self, position: Vector, size: Size) -> bool:
        """Check out of bounds."""
        return (
            position.x < 0
            or position.x + size.width > self.size.width
            or position.y < 0
            or position.y + size.height > self.size.height
        )

    def add_entity(self, entity: Entity) -> None:
        """Add entity."""
        self.entities.append(entity)

    def remove_entity(self, entity: Entity) -> None:
        """Remove entity."""
        self.entities.remove(entity)
