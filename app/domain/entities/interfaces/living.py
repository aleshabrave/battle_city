class Living:
    """Абстрактный класс объектов, у которых есть запрос прочности."""

    def __init__(self, health_points: int):
        if health_points <= 0:
            raise ValueError(
                f"Health points should be positive, but health_points={health_points}"
            )
        self.health_points = health_points

    def take_damage(self, damage: int) -> None:
        """Принять урон."""
        if damage <= 0:
            raise ValueError(f"Damage should be positive, but damage={damage}")
        self.health_points = max(0, self.health_points - damage)

    def is_available(self) -> bool:
        """Проверить жив ли объект."""
        return self.health_points > 0
