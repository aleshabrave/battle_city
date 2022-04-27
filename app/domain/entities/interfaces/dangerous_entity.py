from entity import Entity
from living_entity import LivingEntity

from app.domain.data.params import Size, Vector


class DangerousEntity(Entity):
    """Абстрактный класс опасных сущностей."""

    def __init__(self, name: str, location: Vector, size: Size, damage: int) -> None:
        """Конструктор абстрактного класса DangerousEntity."""
        super().__init__(name, location, size)
        self.damage = damage

    def do_damage(self, enemy: LivingEntity) -> None:
        """Нанести урон."""
        enemy.take_damage(self.damage)
