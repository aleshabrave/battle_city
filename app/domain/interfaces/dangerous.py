from dataclasses import dataclass

from app.domain.interfaces.living import Living


@dataclass
class Dangerous:
    """Абстрактный класс опасных объектов."""

    damage: int

    def __post_init__(self):
        if self.damage <= 0:
            raise ValueError(f"Damage should be positive, but damage={self.damage}")

    def do_damage(self, enemy: Living) -> None:
        """Нанести урон."""
        enemy.take_damage(self.damage)
