from app.domain.data import Direction, Size, Vector
from app.domain.entities.bullet import Bullet, BulletSchema

from .interfaces import Living, MovableEntity

DEFAULT_TANK_SPEED = 2
DEFAULT_TANK_HEALTH_POINTS = 3


class Tank(MovableEntity, Living):
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
        Living.__init__(self, health_points)
        MovableEntity.__init__(self, name, location, size, speed, direction)
        self._bullet_schema = bullet_schema

    def get_bullet(self) -> Bullet:
        """Получить снаряд."""
        return Bullet(
            name=self._bullet_schema.name,
            location=self._get_location_for_bullet(),
            size=self._bullet_schema.size,
            damage=self._bullet_schema.damage,
            speed=self._bullet_schema.speed,
            direction=self.direction,
        )

    def _get_location_for_bullet(self) -> Vector:
        """Получить локацию пули."""
        shift = self.size // 2
        return Vector(self.location.x + shift.width, self.location.y + shift.height)
