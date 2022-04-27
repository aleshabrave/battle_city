from app.domain.data import Size, Vector
from app.domain.entities.details.bullet import Bullet
from app.domain.entities.interfaces import Entity


class Gun(Entity):
    """Класс пушки."""

    def __init__(
        self,
        name: str,
        location: Vector,
        size: Size,
        bullet_size: Size,
        bullet_damage: int,
        bullet_speed: int,
        bullet_direction: float,
    ):
        """Конструктор класса Gun."""
        super().__init__(name, location, size)
        self._bullet_size = bullet_size
        self._bullet_damage = bullet_damage
        self._bullet_speed = bullet_speed
        self._bullet_direction = bullet_direction

    def get_bullet(self) -> Bullet:
        """Получить снаряд."""
        return Bullet(
            "bullet",
            self.location,
            self._bullet_size,
            self._bullet_damage,
            self._bullet_speed,
            self._bullet_direction,
        )
