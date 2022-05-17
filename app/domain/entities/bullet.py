from dataclasses import dataclass

from app.domain.data import Size, Vector
from app.domain.data.enums import Direction
from app.domain.entities.interfaces import Dangerous, MovableEntity

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
