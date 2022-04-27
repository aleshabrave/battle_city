from gun import Gun

from app.domain.data import Size, Vector
from app.domain.entities.interfaces import MoveableEntity


class Body(MoveableEntity):
    """Класс тела танка."""

    def __init__(
        self,
        name: str,
        location: Vector,
        size: Size,
        speed: int,
        direction: float,
        gun: Gun,
    ):
        """Конструктор класса Body."""
        super().__init__(name, location, size, speed, direction)
        self._gun = gun

    def update_location(self) -> Vector:
        """Обновить позицию и про башню не забыть."""
        shift = super(Body, self).update_location()
        self._gun.location.add(shift)
        return shift
