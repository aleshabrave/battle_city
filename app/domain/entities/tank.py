from app.domain.data import Direction, Size, Vector
from app.domain.entities.details.bullet import Bullet, BulletSchema

from .interfaces import Entity, Living, Moveable

DEFAULT_TANK_SPEED = 2
DEFAULT_TANK_HEALTH_POINTS = 3


class Tank(Moveable, Living, Entity):
    """Класс сущности танк."""

    def __init__(
        self,
        name: str,
        location: Vector,
        size: Size,
        speed: int,
        direction: Direction,
        health_points: int,
        bullet_schema: BulletSchema,
    ) -> None:
        Entity.__init__(self, name, location, size)
        Living.__init__(self, health_points)
        Moveable.__init__(self, speed, direction)
        self._bullet_schema = bullet_schema

    def get_bullet(self) -> Bullet:
        """Получить снаряд."""

        return Bullet(
            name=self._bullet_schema.name,
            location=self._bullet_schema.location,
            size=self._bullet_schema.size,
            damage=self._bullet_schema.damage,
            speed=self._bullet_schema.speed,
            direction=self.direction,
        )
