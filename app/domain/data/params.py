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


def are_intersected(source: tuple[Vector, Size], other: tuple[Vector, Size]) -> bool:
    return (
        source[0].x + source[1].width > other[0].x
        and source[0].y < other[0].y + other[1].height
        and other[0].x + other[1].width > source[0].x
        and other[0].y < source[0].y + source[1].height
    )
