from .living import Living


class Dangerous:
    """Абстрактный класс опасных объектов."""

    def __init__(self, damage: int) -> None:
        self.damage = damage

    def do_damage(self, enemy: Living) -> None:
        """Нанести урон."""
        enemy.take_damage(self.damage)
