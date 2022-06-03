from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Vector:
    """Класс вектора."""

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

    def dist_to(self, other: "Vector") -> int:
        """Расстояние."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


@dataclass(unsafe_hash=True)
class Size:
    """Класс размера."""

    width: int
    height: int

    def __mul__(self, scalar: int) -> "Size":
        """Умножить на скаляр."""
        width = self.width * scalar
        height = self.height * scalar
        return Size(width, height)


class Methods:
    @staticmethod
    def are_intersected(
        source: tuple[Vector, Size], other: tuple[Vector, Size]
    ) -> bool:
        return (
            source[0].x + source[1].width > other[0].x
            and source[0].y < other[0].y + other[1].height
            and other[0].x + other[1].width > source[0].x
            and other[0].y < source[0].y + source[1].height
        )
