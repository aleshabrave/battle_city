from app.domain import Map
from app.domain.entities.details import Bullet
from app.domain.entities.interfaces import Dangerous, Living, Movable, Entity
from typing import Union


class MapController:
    """Класс контроллера для Map."""

    def __init__(self, _map: Map) -> None:
        self.map = _map

    def update_map(self):
        self.move_entities()
        self.resolve_move_conflicts()
        self.resolve_dangerous_conflicts()

    def move_entities(self) -> None:
        """Подвинуть moveable entities."""

        for entity in self.map.entities:
            if isinstance(entity, Movable):
                entity.update_location()

    def resolve_dangerous_conflicts(self) -> None:
        """Разрешить ситуации с взаимодействием опасных сущностей."""

        for entity in self.map.entities:
            if not isinstance(entity, Dangerous):
                continue
            neighbour = self.map.get_neighbour(entity)
            if neighbour is not None and isinstance(neighbour, Living):
                neighbour.take_damage(entity.damage)
                if isinstance(entity, Bullet):
                    self.map.remove_entity(entity)

    def resolve_move_conflicts(self) -> None:
        """Разрешить столкновения сущностей."""

        for entity in self.map.entities:
            if not isinstance(entity, Movable):
                continue

            neighbour = self.map.get_neighbour(entity)
            if isinstance(neighbour, Living):
                self._resolve_move_conflict_with_other_entity(entity, neighbour)

            if self.map.check_out_of_bounds(entity):
                self._resolve_out_of_bounds(entity)

    def _resolve_out_of_bounds(self, mover: Union[Movable, Entity]) -> None:
        """Разрешить выход за пределы карты."""

        if mover.location.x < 0:
            mover.location.x = 0
        if mover.location.y < 0:
            mover.location.y = 0
        if mover.location.x + mover.size.width >= self.map.size.width:
            mover.location.x = self.map.size.width - mover.size.width - 1
        if mover.location.y + mover.size.height >= self.map.size.height:
            mover.location.y = self.map.size.height - mover.size.height - 1

    @staticmethod
    def _resolve_move_conflict_with_other_entity(
        mover: Union[Movable, Entity], entity: Union[Living, Entity]
    ) -> None:
        """Разрешить столкновение сущности (если оно есть)."""

        if mover.location.x <= entity.location.x + entity.size.width:
            mover.location.x = entity.location.x + entity.size.width + 1
        if mover.location.x + mover.size.width >= entity.location.x:
            mover.location.x = entity.location.x - mover.size.width - 1
        if mover.location.y <= entity.location.y + entity.size.height:
            mover.location.y = entity.location.y + entity.size.height + 1
        if mover.location.y + mover.size.height >= entity.location.y:
            mover.location.y = entity.location.y - mover.size.height - 1
