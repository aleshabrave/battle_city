import math

from app.domain.data import Direction, Size, Vector
from app.domain.entities.interfaces import Entity
from app.domain.map import Map


class MovableEntity(Entity):
    """Абстрактный класс объектов, которые могут двигаться."""

    def __init__(
        self, name: str, location: Vector, size: Size, speed: int, direction: Direction
    ):
        super().__init__(name, location, size)
        self.speed = speed
        self.direction = direction

    def update_location(self, map_: Map) -> None:
        """Обновить позицию сущности."""
        if self.name == "player":
            print(self.location)
            print(self.speed)
            print(self.direction)

        shift = Vector(
            int(math.cos(self.direction.value) * self.speed),
            int(math.sin(self.direction.value) * self.speed),
        )
        new_location = self.location + shift

        if map_.check_out_of_bounds(new_location, self.size):
            self._resolve_out_of_bounds(new_location, map_)
            return

        shift_size = Size(
            abs(new_location.x - self.location.x) + self.size.width - 1,
            abs(new_location.y - self.location.y) + self.size.height - 1,
        )
        conflict_entities = list(
            filter(
                lambda x: id(x) != id(self),
                map_.get_entities_by_location(self.location, shift_size),
            )
        )

        if not conflict_entities:
            self.location = new_location
            return

        if self.direction == Direction.UP:
            entity = min(
                conflict_entities,
                key=lambda z: abs(z.location.y - self.location.y - self.size.height),
            )
            new_location.y = entity.location.y - self.size.height - 1
        elif self.direction == Direction.DOWN:
            entity = min(
                conflict_entities,
                key=lambda z: abs(z.location.y + z.size.height - self.location.y),
            )
            new_location.y = entity.location.y + entity.size.height
        elif self.direction == Direction.LEFT:
            entity = min(
                conflict_entities,
                key=lambda z: abs(z.location.x + z.size.width - self.location.x),
            )
            new_location.x = entity.location.x + entity.size.width
        elif self.direction == Direction.RIGHT:
            entity = min(
                conflict_entities,
                key=lambda z: abs(z.location.y + z.size.height - self.location.y),
            )
            new_location.x = entity.location.x - self.size.width - 1

        self.location = new_location

    def is_moving(self) -> bool:
        """Проверка на движение."""
        return self.speed != 0

    def _resolve_out_of_bounds(self, new_location: Vector, map_: Map) -> None:
        """Разрешить выход за пределы карты."""
        if new_location.x < 0:
            self.location.x = 0
        if new_location.y < 0:
            self.location.y = 0
        if new_location.x + self.size.width >= map_.size.width:
            self.location.x = map_.size.width - self.size.width - 1
        if new_location.y + self.size.height >= map_.size.height:
            self.location.y = map_.size.height - self.size.height - 1
