from dataclasses import dataclass


@dataclass
class Vector:
    """Класс Vector."""

    x: int
    y: int
    z: int = 3  # индекс для отрисовки

    def add(self, other: "Vector") -> None:
        """Добавить вектор."""
        self.x += other.x
        self.y += other.y


@dataclass
class Size:
    """Дата класс для размера."""

    width: int
    height: int
