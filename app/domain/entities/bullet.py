import math
from dataclasses import dataclass

from app.domain.data import Size, Vector
from app.domain.data.enums import Direction
from app.domain.entities.interfaces import Dangerous, Living, MovableEntity
from app.domain.map import Map

DEFAULT_DAMAGE = 1


@dataclass
class BulletSchema:
    name: str
    size: Size
    damage: int
    speed: int


class Bullet(Dangerous, MovableEntity):
    """Класс снаряда."""

    def __init__(
        self,
        name: str,
        location: Vector,
        size: Size,
        damage: int,
        speed: int,
        direction: Direction,
    ):
        """Конструктор класса Bullet."""
        Dangerous.__init__(self, damage)
        MovableEntity.__init__(self, name, location, size, speed, direction)

    def update_location(self, map_: Map) -> None:
        shift = Vector(
            int(math.cos(self.direction.value) * self.speed),
            int(math.sin(self.direction.value) * self.speed),
        )
        self.location += shift

        neighbours = map_.get_neighbours(self)
        if not neighbours:
            return

        for neighbour in neighbours:
            if isinstance(neighbour, Living):
                if self.name == "player_bullet" and neighbour.name == "player":
                    continue
                if self.name == "enemy_bullet" and neighbour.name == "enemy_tank":
                    map_.remove_entity(self)
                    return

                if not self.name == "player_bullet" or not neighbour.name == "castle":
                    neighbour.take_damage(self.damage)

                if not neighbour.is_available():
                    map_.remove_entity(neighbour)
                map_.remove_entity(self)
                return
