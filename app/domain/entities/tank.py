from interfaces import LivingEntity

from app.domain.entities.details.body import Body
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
