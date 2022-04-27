import math

from entity import Entity

from app.domain.data import Size, Vector


class MoveableEntity(Entity):
    """Абстрактный класс сущностей, которые могут двигаться."""

    def __init__(
        self, name: str, location: Vector, size: Size, speed: int, direction: float
    ):
        """Конструктор абстрактного класса MoveableEntity."""
        super().__init__(name, location, size)
        self._speed = speed
        self._direction = direction

    def update_location(self) -> Vector:
        """Обновить позицию сущности и получить смещение."""
        shift = Vector(
            int(math.cos(self._direction) * self._speed),
            int(math.sin(self._direction) * self._speed),
        )
        self.location.add(shift)
        return shift
