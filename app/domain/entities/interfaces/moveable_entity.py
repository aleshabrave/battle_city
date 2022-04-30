import math

from app.domain.data import Size, Vector

from .entity import Entity


class MoveableEntity(Entity):
    """Абстрактный класс сущностей, которые могут двигаться."""

    def __init__(
        self, name: str, location: Vector, size: Size, speed: int, direction: float
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
    def direction(self) -> float:
        return self._direction

    @direction.setter
    def direction(self, new: float) -> None:
        self._direction = new

    def update_location(self) -> Vector:
        """Обновить позицию сущности и получить смещение."""
        shift = Vector(
            int(math.cos(self._direction) * self._speed),
            int(math.sin(self._direction) * self._speed),
        )
        self.location += shift
        return shift
