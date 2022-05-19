from app.domain.data import Direction, Size, Vector
from app.domain.entities.bullet import Bullet, BulletSchema

from .interfaces import Living, MovableEntity

DEFAULT_TANK_SPEED = 4
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
            location=self._get_bullet_location(self._bullet_schema.size),
            size=self._bullet_schema.size,
            damage=self._bullet_schema.damage,
            speed=self._bullet_schema.speed,
            direction=self.direction,
        )

    def _get_bullet_location(self, bullet_size: Size) -> Vector:
        """Получить локацию пули."""
        if self.direction == Direction.DOWN:
            shift = Vector(
                self.size.width // 2 - bullet_size.width // 2, -1 - bullet_size.height
            )
        elif self.direction == Direction.UP:
            shift = Vector(
                self.size.width // 2 - bullet_size.width // 2, self.size.height + 1
            )
        elif self.direction == Direction.RIGHT:
            shift = Vector(
                self.size.width + 1, self.size.height // 2 - bullet_size.height // 2
            )
        else:
            shift = Vector(
                -1 - bullet_size.width, self.size.height // 2 - bullet_size.height // 2
            )
        return self.location + shift
