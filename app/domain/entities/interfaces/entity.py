from app.domain.data.params import Size, Vector


class Entity:
    """Абстрактный класс сущности."""

    def __init__(self, name: str, location: Vector, size: Size) -> None:
        self.name = name
        self.location = location
        self.size = size

    def move(self, shift: Vector) -> None:
        """Переместить объект."""
        self.location += shift
