from dataclasses import dataclass

from app.domain.data import Size, Vector
from app.domain.data.enums import Direction
from app.domain.entities.interfaces import Dangerous, Entity, Movable

DEFAULT_DAMAGE = 1


@dataclass
class BulletSchema:
    name: str
    location: Vector
    size: Size
    damage: int
    speed: int


class Bullet(Dangerous, Movable, Entity):
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
        Entity.__init__(self, name, location, size)
        Dangerous.__init__(self, damage)
        Movable.__init__(self, speed, direction)
