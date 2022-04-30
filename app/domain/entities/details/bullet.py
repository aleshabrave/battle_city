from app.domain.data import Size, Vector
from app.domain.data.enums import Direction
from app.domain.entities.interfaces import DangerousEntity, MoveableEntity

DEFAULT_DAMAGE = 1


class Bullet(DangerousEntity, MoveableEntity):
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
        super().__init__(name, location, size, damage)
        self.speed = speed
        self.direction = direction
