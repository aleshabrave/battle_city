import math
from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from app.domain.enums import Direction
from app.domain.interfaces.entity import Entity
from app.domain.utils import Size, Vector

if TYPE_CHECKING:
    from app.domain.map import Map


@dataclass
class Movable(Entity):
    """Абстрактный класс сущностей, которые могут двигаться."""

    speed: int
    direction: Direction

    def update_location(
        self, map_: "Map", out_of_bound_remove_flag: bool = False
    ) -> Optional[Entity]:
        """Обновить позицию сущности."""
        new_position = self._get_new_position()

        if map_.check_out_of_bounds(new_position, self.size):
            if out_of_bound_remove_flag:
                map_.remove_entity(self)
            else:
                self.position = self._resolve_out_of_bounds(
                    new_position, self.size, map_.size
                )
            return

        conflict_entities = self._get_conflict_entities(new_position, map_)

        if not conflict_entities:
            self.position = new_position
            return

        return self._resolve_conflicts_with_other_entities(conflict_entities)

    def is_moving(self) -> bool:
        """Проверка на движение."""
        return self.speed != 0

    def _get_new_position(self) -> Vector:
        """Получить новую позицию."""
        shift = Vector(
            int(math.cos(self.direction.value) * self.speed),
            int(math.sin(self.direction.value) * self.speed),
        )
        return self.position + shift

    def _get_conflict_entities(self, new_position: Vector, map_: "Map") -> list[Entity]:
        """Получить сущностей, которые могут помешать движению (кроме снарядов)."""
        shift_size = Size(
            abs(new_position.x - self.position.x) + self.size.width,
            abs(new_position.y - self.position.y) + self.size.height,
        )
        entities = (
            map_.get_entities_by_location(new_position, shift_size)
            if self.direction == Direction.LEFT or self.direction == Direction.DOWN
            else map_.get_entities_by_location(self.position, shift_size)
        )
        return list(
            filter(
                lambda x: id(x) != id(self),
                entities,
            )
        )

    @staticmethod
    def _resolve_out_of_bounds(
        new_position: Vector, size: Size, map_size: Size
    ) -> Vector:
        """Разрешить выход за пределы карты."""
        result_position = Vector(new_position.x, new_position.y)
        if new_position.x < 0:
            result_position.x = 0
        if new_position.y < 0:
            result_position.y = 0
        if new_position.x + size.width > map_size.width:
            result_position.x = map_size.width - size.width
        if new_position.y + size.height > map_size.height:
            result_position.y = map_size.height - size.height
        return result_position

    def _resolve_conflicts_with_other_entities(
        self, conflict_entities: list[Entity]
    ) -> Entity:
        """Разрешить столкновение с другими сущностями."""
        if self.direction == Direction.UP:
            entity = min(
                conflict_entities,
                key=lambda z: abs(z.position.y - self.position.y - self.size.height),
            )
            self.position.y = entity.position.y - self.size.height - 1
        elif self.direction == Direction.DOWN:
            entity = min(
                conflict_entities,
                key=lambda z: abs(z.position.y + z.size.height - self.position.y),
            )
            self.position.y = entity.position.y + entity.size.height + 1
        elif self.direction == Direction.LEFT:
            entity = min(
                conflict_entities,
                key=lambda z: abs(z.position.x + z.size.width - self.position.x),
            )
            self.position.x = entity.position.x + entity.size.width + 1
        else:
            entity = min(
                conflict_entities,
                key=lambda z: abs(z.position.y + z.size.height - self.position.y),
            )
            self.position.x = entity.position.x - self.size.width - 1

        return entity
