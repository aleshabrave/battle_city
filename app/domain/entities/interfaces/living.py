from abc import abstractmethod


class Living:
    """Абстрактный класс объектов, у которых есть запрос прочности."""

    def __init__(self, health_points: int):
        self.health_points = health_points

    @abstractmethod
    def take_damage(self, damage: int) -> None:
        """Принять урон."""

    def is_available(self) -> bool:
        """Проверить жив ли объект."""

        return self.health_points > 0
