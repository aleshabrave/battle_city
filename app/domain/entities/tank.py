from app.domain.entities.details.body import Body
from app.domain.entities.details.gun import Gun

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
