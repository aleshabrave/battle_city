from dataclasses import dataclass

from app.domain.data.enums import Direction
from app.domain.entities.tank import Tank
from app.domain.map import Map


@dataclass
class TankController:
    """Контроллер для сущности Tank"""

    _tank: Tank

    def update_speed(self, speed: int) -> None:
        """Обновить скорость танка."""
        self._tank.speed = speed

    def update_direction(self, direction: Direction) -> None:
        """Обновить направление движения танка."""
        self._tank.direction = direction

    def take_damage(self, damage: int) -> None:
        """Принять урон."""
        self._tank.take_damage(damage)

    def fire(self, map_: Map) -> None:
        """Выстрелить."""
        map_.add_entity(self._tank.get_bullet())
