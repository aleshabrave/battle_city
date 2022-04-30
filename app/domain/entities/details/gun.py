from app.domain.data import Size, Vector
from app.domain.data.enums import Direction
from app.domain.entities.details.bullet import Bullet
from app.domain.entities.interfaces import MoveableEntity


class Gun(MoveableEntity):
    """Класс пушки."""

    def __init__(
        self,
        name: str,
        location: Vector,
        size: Size,
        speed: int,
        direction: Direction,
        bullet_size: Size,
        bullet_damage: int,
        bullet_speed: int,
    ) -> None:
        """Конструктор класса Gun."""
        super().__init__(name, location, size, speed, direction)
        self._bullet_size = bullet_size
        self._bullet_damage = bullet_damage
        self._bullet_speed = bullet_speed

    def get_bullet(self) -> Bullet:
        """Получить снаряд."""
        return Bullet(
            "bullet",
            self.location,
            self._bullet_size,
            self._bullet_damage,
            self._bullet_speed,
            self._direction,
        )
