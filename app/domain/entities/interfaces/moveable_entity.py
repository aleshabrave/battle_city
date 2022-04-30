import math

from app.domain.data import Size, Vector

from ...data.enums import Direction
from .entity import Entity


class MoveableEntity(Entity):
    """Абстрактный класс сущностей, которые могут двигаться."""

    def __init__(
        self, name: str, location: Vector, size: Size, speed: int, direction: Direction
    ):
        """Конструктор абстрактного класса MoveableEntity."""
        super().__init__(name, location, size)
        self._speed = speed
        self._direction = direction

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    def speed(self, new: int) -> None:
        self.speed = new

    @property
    def direction(self) -> Direction:
        return self._direction

    @direction.setter
    def direction(self, new: Direction) -> None:
        self._direction = new

    def update_location(self) -> Vector:
        """Обновить позицию сущности и получить смещение."""
        shift = Vector(
            int(math.cos(self._direction.value) * self._speed),
            int(math.sin(self._direction.value) * self._speed),
        )
        self.location += shift
        return shift
