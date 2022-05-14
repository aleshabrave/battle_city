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

    @staticmethod
    def are_intersected(entity1: "Entity", entity2: "Entity") -> bool:
        """Проверка на пересечение."""
        return (
                entity1.location.x + entity1.size.width >= entity2.location.x
                and entity1.location.y <= entity2.location.y + entity2.size.height
                and entity2.location.x + entity2.size.width >= entity1.location.x
                and entity2.location.y <= entity1.location.y + entity1.size.height
        )
