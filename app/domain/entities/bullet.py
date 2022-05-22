from dataclasses import dataclass

from app.domain.enums import Direction
from app.domain.interfaces import Dangerous, Living, Movable
from app.domain.map import Map
from app.domain.utils import Size, Vector


@dataclass(unsafe_hash=True)
class BulletSchema:
    name: str
    size: Size
    damage: int
    speed: int


@dataclass
class Bullet(Movable, Dangerous):
    """Класс снаряда."""

    def update_location(self, map_: Map, **kwargs: dict) -> None:
        """Обновить позицию снаряда."""
        entity = Movable.update_location(self, map_=map_, out_of_bound_remove_flag=True)

        if entity is not None:
            if isinstance(entity, Living):
                self.do_damage(entity)
                if not entity.is_available():
                    map_.remove_entity(entity)

            if isinstance(entity, Bullet):
                map_.remove_entity(entity)

            map_.remove_entity(self)


@dataclass(unsafe_hash=True)
class BulletFactory:
    """Класс фабрики снарядов."""

    _bullet_schema: BulletSchema

    def create(self, position: Vector, direction: Direction) -> Bullet:
        """Создать снаряд."""
        return Bullet(
            name=self._bullet_schema.name,
            size=self._bullet_schema.size,
            speed=self._bullet_schema.speed,
            position=position,
            direction=direction,
            damage=self._bullet_schema.damage,
        )
