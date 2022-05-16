from dataclasses import dataclass


@dataclass
class Vector:
    """Класс Vector."""

    x: int
    y: int

    def __add__(self, other: "Vector") -> "Vector":
        """Добавить вектор."""
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: int) -> "Vector":
        """Умножить на скаляр."""
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)


@dataclass
class Size:
    """Дата класс для размера."""

    width: int
    height: int

    def __mul__(self, scalar: int) -> "Size":
        """Умножить на скаляр."""
        width = self.width * scalar
        height = self.height * scalar
        return Size(width, height)

    def __floordiv__(self, scalar: int) -> "Size":
        """Поделить на скаляр."""
        width = (abs(self.width) // abs(scalar)) * (self.width // abs(self.width)) * (scalar // abs(scalar))
        height = (abs(self.height) // abs(scalar)) * (self.height // abs(self.height)) * (scalar // abs(scalar))
        return Size(width, height)
