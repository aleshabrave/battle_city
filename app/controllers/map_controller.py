from app.domain import Map
from app.domain.entities.details import Bullet
from app.domain.entities.interfaces import Dangerous, Living, Moveable


class MapController:
    """Класс контроллера для Map."""

    def __init__(self, _map: Map) -> None:
        self._map = _map

    def move_entities(self) -> None:
        """Подвинуть moveable entities."""

        for entity in self._map._entities:
            if isinstance(entity, Moveable):
                entity.update_location()

    def resolve_dangerous_conflicts(self) -> None:
        """Разрешить ситуации с взаимодействием опасных сущностей."""

        for entity in self._map._entities:
            if not isinstance(entity, Dangerous):
                continue
            neighbour = self._map.get_neighbour(entity)
            if neighbour is not None and isinstance(neighbour, Living):
                neighbour.take_damage(entity.damage)
                if isinstance(entity, Bullet):
                    self._map.remove_entity(entity)

    def resolve_move_conflicts(self) -> None:
        """Разрешить столкновения сущностей."""

        for entity in self._map._entities:
            if not isinstance(entity, Moveable):
                continue

            neighbour = self._map.get_neighbour(entity)
            if isinstance(neighbour, Living):
                self._resolve_move_conflict_with_other_entity(entity, neighbour)

            if self._map.check_out_of_bounds(entity):
                self._resolve_out_of_bounds(entity)

    def _resolve_out_of_bounds(self, mover: Moveable) -> None:
        """Разрешить выход за пределы карты."""

    @staticmethod
    def _resolve_move_conflict_with_other_entity(
        mover: Moveable, entity: Living
    ) -> None:
        """Разрешить столкновение сущности."""
