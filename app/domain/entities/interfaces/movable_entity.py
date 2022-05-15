import math

from app.domain.data import Direction, Vector, Size
from app.domain.entities.interfaces import Entity


class MovableEntity(Entity):
    """Абстрактный класс объектов, которые могут двигаться."""

    def __init__(
        self, name: str, location: Vector, size: Size, speed: int, direction: Direction
    ):
        super().__init__(name, location, size)
        self.speed = speed
        self.direction = direction

    def update_location(self) -> Vector:
        """Обновить позицию сущности и получить смещение."""
        shift = Vector(
            int(math.cos(self.direction.value) * self.speed),
            int(math.sin(self.direction.value) * self.speed),
        )
        self.location += shift
        return shift

    def is_moving(self) -> bool:
        """Проверка на движение."""
        return self.speed != 0
