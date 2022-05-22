from dataclasses import dataclass

from app.domain.entities.bullet import Bullet, BulletFactory, BulletSchema
from app.domain.enums import Direction
from app.domain.interfaces import Living, Movable
from app.domain.utils import Size, Vector


@dataclass(unsafe_hash=True)
class Tank(Movable, Living):
    """Класс сущности танк."""

    _bullet_schema: BulletSchema
    _bullet_factory: BulletFactory = None

    def __post_init__(self):
        self._bullet_factory = BulletFactory(self._bullet_schema)

    def get_bullet(self) -> Bullet:
        """Получить снаряд."""

        return self._bullet_factory.create(
            position=self._get_bullet_position(self._bullet_schema.size),
            direction=self.direction,
        )

    def _get_bullet_position(self, bullet_size: Size) -> Vector:
        """Получить позицию пули."""
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
        return self.position + shift
