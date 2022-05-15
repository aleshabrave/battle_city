from app.domain.data import Direction, Size, Vector
from app.domain.entities.details.bullet import Bullet, BulletSchema

from .interfaces import Entity, Living, Movable

DEFAULT_TANK_SPEED = 2
DEFAULT_TANK_HEALTH_POINTS = 3


class Tank(Movable, Living, Entity):
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
        Movable.__init__(self, speed, direction)
        self._bullet_schema = bullet_schema

    def get_bullet(self) -> Bullet:
        """Получить снаряд."""

        return Bullet(
                name=self._bullet_schema.name,
                location=self._calculate_location_for_bullet(),
                size=self._bullet_schema.size,
                damage=self._bullet_schema.damage,
                speed=self._bullet_schema.speed,
                direction=self.direction,
                )

    def _calculate_location_for_bullet(self):
        if self.direction == Direction.DOWN or self.direction == Direction.LEFT:
            return self.location
        if self.direction == Direction.RIGHT:
            return self.location + Vector(self.size.width, 0)
        return self.location + Vector(0, self.size.height)
