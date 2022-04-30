from app.domain.entities.details.body import Body
from app.domain.entities.details.bullet import Bullet
from app.domain.entities.details.gun import Gun

from ..data.enums import Direction
from .interfaces import LivingEntity

DEFAULT_TANK_SPEED = 2
DEFAULT_TANK_HEALTH_POINTS = 3


class Tank(LivingEntity):
    """Класс сущности танк."""

    def __init__(
        self,
        name: str,
        gun: Gun,
        body: Body,
        health_points: int,
    ) -> None:
        """Конструктор класса Tank."""
        super().__init__(name, body.location, body.size, health_points)
        self._gun = gun
        self._body = body

    def update_location(self) -> None:
        """Обновить позиции основы и пушки танка"""
        self._body.update_location()
        self._gun.update_location()

    def change_speed(self, added_value: int) -> None:
        """Изменяет скорость танка."""
        self._body.speed += added_value
        self._gun.speed += added_value

    def change_body_direction(self, new_dir: Direction) -> None:
        """Изменяет направление движения танка."""
        self._body.direction = new_dir.value

    def change_gun_direction(self, new_dir: Direction) -> None:
        """Изменяет направление пушки."""
        self._gun.direction = new_dir

    def get_bullet(self) -> Bullet:
        """Получить снаряд."""
        return self._gun.get_bullet()
