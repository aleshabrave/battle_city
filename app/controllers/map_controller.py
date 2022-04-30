from app.domain import Map
from app.domain.entities.details import Bullet
from app.domain.entities.interfaces import DangerousEntity, LivingEntity, MoveableEntity


class MapController:
    """Класс контроллера для Map."""

    def __init__(self, _map: Map) -> None:
        self._map = _map

    def resolve_dangerous_conflicts(self) -> None:
        """Разрешить ситуации с взаимодействием опасных сущностей."""

        for entity in self._map.entities:
            if not isinstance(entity, DangerousEntity):
                continue
            neighbour = self._map.get_neighbour(entity)
            if neighbour is not None and isinstance(neighbour, LivingEntity):
                neighbour.take_damage(entity.damage)
                if isinstance(entity, Bullet):
                    self._map.remove_entity(entity)

    def resolve_move_conflicts(self) -> None:
        """Разрешить столкновения сущностей."""

        for entity in self._map.entities:
            if not isinstance(entity, MoveableEntity):
                continue

            neighbour = self._map.get_neighbour(entity)
            if isinstance(neighbour, LivingEntity):
                self._resolve_move_conflict_with_other_entity(entity, neighbour)

            if self._map.check_out_of_bounds(entity):
                self._resolve_out_of_bounds(entity)

    def _resolve_out_of_bounds(self, mover: MoveableEntity) -> None:
        """Разрешить выход за пределы карты."""

    @staticmethod
    def _resolve_move_conflict_with_other_entity(
        mover: MoveableEntity, entity: LivingEntity
    ) -> None:
        """Разрешить столкновение сущности."""
