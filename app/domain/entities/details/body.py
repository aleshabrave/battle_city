from app.domain.data import Size, Vector
from app.domain.entities.interfaces import MoveableEntity


class Body(MoveableEntity):
    """Класс тела танка."""

    def __init__(
        self, name: str, location: Vector, size: Size, speed: int, direction: float
    ):
        """Конструктор класса Body."""
        super().__init__(name, location, size, speed, direction)

    def update_location(self) -> Vector:
        """Обновить позицию"""
        shift = super(Body, self).update_location()
        return shift
