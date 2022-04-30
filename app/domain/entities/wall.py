from app.domain.data import Size, Vector

from .interfaces import Entity, Living

DEFAULT_WALL_HEALTH_POINTS = 3


class Wall(Living, Entity):
    """Класс стены."""

    def __init__(
        self, name: str, location: Vector, size: Size, health_points: int
    ) -> None:
        Entity.__init__(self, name, location, size)
        Living.__init__(self, health_points)
