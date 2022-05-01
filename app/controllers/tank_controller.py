from app.domain.data.enums import Direction
from app.domain.entities.tank import Tank
from app.domain.map import Map


class TankController:
    """Контроллер для сущности Tank"""

    def __init__(self, tank: Tank):
        self._tank = tank

    def update_speed(self, speed: int) -> None:
        """Обновить скорость танка."""
        self._tank.speed = speed

    def update_direction(self, direction: Direction) -> None:
        """Обновить направление движения танка."""
        self._tank.direction = direction

    def take_damage(self, damage: int) -> None:
        """Принять урон."""
        self._tank.take_damage(damage)

    def fire(self, _map: Map) -> None:
        """Выстрелить."""
        _map.add_entity(self._tank.get_bullet())
