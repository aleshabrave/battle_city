from app.domain.data import Size, Vector
from app.domain.entities.interfaces import DangerousEntity, MoveableEntity


class Bullet(DangerousEntity, MoveableEntity):
    """Класс снаряда."""

    def __init__(
        self,
        name: str,
        location: Vector,
        size: Size,
        damage: int,
        speed: int,
        direction: float,
    ):
        """Конструктор класса Bullet."""
        super().__init__(name, location, size, damage)
        self.speed = speed
        self.direction = direction
