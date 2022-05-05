import math

from app.domain.data import Vector
from app.domain.data import Direction


class Moveable:
    """Абстрактный класс объектов, которые могут двигаться."""

    def __init__(self, speed: int, direction: Direction):
        """Конструктор абстрактного класса MoveableEntity."""

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
