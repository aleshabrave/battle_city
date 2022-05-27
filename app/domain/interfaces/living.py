from dataclasses import dataclass

from app.domain.interfaces.observable import Observable


@dataclass
class Living(Observable):
    """Абстрактный класс объектов c health points."""

    health_points: int

    def __post_init__(self):
        if self.health_points <= 0:
            raise ValueError(
                f"Health points should be positive, but health_points={self.health_points}"
            )

    def take_damage(self, damage: int) -> None:
        """Принять урон."""
        if damage <= 0:
            raise ValueError(f"Damage should be positive, but health_points={damage}")
        self.health_points = max(0, self.health_points - damage)
        self.notify()

    def is_available(self) -> bool:
        """Проверить жив ли объект."""
        return self.health_points > 0
