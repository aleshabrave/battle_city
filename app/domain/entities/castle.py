from app.domain.data import Size, Vector
from app.domain.interfaces import Observable

from .interfaces import Entity, Living

DEFAULT_CASTLE_HEALTH_POINTS = 3


class Castle(Living, Entity, Observable):
    """Класс базы."""

    def __init__(self, name: str, location: Vector, size: Size, health_points: int):
        Living.__init__(self, health_points)
        Entity.__init__(self, name, location, size)

    @Observable.notify
    def take_damage(self, damage: int) -> None:
        """Принять урон."""

        self.health_points -= damage
