from app.domain.data.params import Size, Vector

from .entity import Entity


class LivingEntity(Entity):
    """Абстрактный класс живущих сущностей."""

    def __init__(self, name: str, location: Vector, size: Size, health_points: int):
        """Конструктор абстрактного класса LivingEntity."""

        super().__init__(name, location, size)
        self.health_point = health_points

    def take_damage(self, damage: int) -> None:
        """Принять урон."""

        self.health_point -= damage

    def is_available(self) -> bool:
        """Проверить жив ли объект."""

        return self.health_point > 0
