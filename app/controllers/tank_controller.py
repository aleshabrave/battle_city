from app.domain.data.enums import Direction
from app.domain.entities.tank import Tank
from app.domain.map import Map


class TankController:
    """Контроллер для сущности Tank"""

    def __init__(self, tank: Tank):
        self._tank = tank

    def move(self) -> None:
        """Изменяет координаты танка."""
        self._tank.update_location()

    def change_speed(self, added_value: int) -> None:
        """Изменяет скорость танка."""
        self._tank.change_speed(added_value)

    def change_body_direction(self, new_dir: Direction) -> None:
        """Изменяет направление движения танка."""
        self._tank.change_body_direction(new_dir)

    def change_gun_direction(self, new_dir: float) -> None:
        """Изменяет направление пушки."""
        self._tank.change_gun_direction(new_dir)

    def take_damage(self, damage: int) -> None:
        """Принять урон."""
        self._tank.take_damage(damage)

    def shoot(self, map_: Map) -> None:
        """Добавляет снаряд на карту."""
        map_.add_entity(self._tank.get_bullet())
