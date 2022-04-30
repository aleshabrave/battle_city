from interfaces import LivingEntity

from app.domain.data.enums import Direction
from app.domain.entities.details.body import Body
from app.domain.entities.details.bullet import Bullet
from app.domain.entities.details.gun import Gun


class Tank(LivingEntity):
    """Класс сущности танк."""

    def __init__(
        self,
        name: str,
        gun: Gun,
        body: Body,
        health_point: int,
    ) -> None:
        """Конструктор класса Tank."""
        super().__init__(name, body.location, body.size, health_point)
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

    def change_gun_direction(self, new_dir: float) -> None:
        """Изменяет направление пушки."""
        self._gun.direction = new_dir

    def get_bullet(self) -> Bullet:
        """Получить снаряд."""
        return self._gun.get_bullet()
