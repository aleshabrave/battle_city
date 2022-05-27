from unittest.mock import MagicMock

import pytest

from app.domain.enums import Direction
from app.domain.interfaces import Entity, Movable
from app.domain.utils import Size, Vector


class TestsMovable:
    @pytest.mark.parametrize(
        "remove_flag",
        [True, False],
    )
    def test__update_location_if_out_of_map(self, remove_flag):
        entity_obj = MagicMock()
        map_ = MagicMock(check_out_of_bounds=MagicMock(return_value=True))

        actual = Movable.update_location(
            entity_obj, map_, out_of_bound_remove_flag=remove_flag
        )

        if remove_flag:
            map_.remove_entity.assert_called_once_with(entity_obj)
        else:
            assert not map_.remove_entity.called
            entity_obj._resolve_out_of_bounds.assert_called_once_with(
                entity_obj._get_new_position.return_value,
                entity_obj.size,
                map_.size,
            )
            assert entity_obj.position == entity_obj._resolve_out_of_bounds.return_value
        assert actual is None

    def test__update_location_if_not_out_of_map_and_no_conflicts(self):
        entity_obj = MagicMock(_get_conflict_entities=MagicMock(return_value=[]))
        map_ = MagicMock(check_out_of_bounds=MagicMock(return_value=False))

        actual = Movable.update_location(entity_obj, map_)

        assert entity_obj.position == entity_obj._get_new_position.return_value
        assert actual is None

    def test__update_location_if_not_out_of_map_and_some_conflicts(self):
        entity_obj = MagicMock()
        map_ = MagicMock(check_out_of_bounds=MagicMock(return_value=False))

        actual = Movable.update_location(entity_obj, map_)

        assert actual == entity_obj._resolve_conflicts_with_other_entities(
            entity_obj._get_conflict_entities.return_value
        )

    @pytest.mark.parametrize("speed,expected", [(1, True), (-1, True), (0, False)])
    def test__is_moving(self, speed, expected):
        entity = MagicMock(speed=speed)

        actual = Movable.is_moving(entity)

        assert actual == expected

    @pytest.mark.parametrize(
        "position,size,map_size,expected",
        [
            (Vector(4, 0), Size(2, 2), Size(3, 3), Vector(1, 0)),
            (Vector(0, 4), Size(2, 2), Size(3, 3), Vector(0, 1)),
            (Vector(-1, 0), Size(2, 2), Size(2, 2), Vector(0, 0)),
            (Vector(0, -1), Size(2, 2), Size(2, 2), Vector(0, 0)),
            (Vector(-1, -1), Size(2, 2), Size(2, 2), Vector(0, 0)),
        ],
    )
    def test__resolve_out_of_bounds(self, position, size, map_size, expected):
        actual = Movable._resolve_out_of_bounds(position, size, map_size)

        assert actual == expected

    @pytest.mark.parametrize(
        "direction,speed,expected",
        [
            (Direction.UP, 1, Vector(0, 1)),
            (Direction.DOWN, 1, Vector(0, -1)),
            (Direction.RIGHT, 1, Vector(1, 0)),
            (Direction.LEFT, 1, Vector(-1, 0)),
        ],
    )
    def test__get_new_position(self, direction, speed, expected):
        entity_obj = MagicMock(direction=direction, speed=speed)

        actual = Movable._get_new_position(entity_obj)

        assert actual == entity_obj.position + expected

    @pytest.mark.parametrize(
        "entity,entities,expected_entity,expected_position",
        [
            (
                Movable("1", Vector(1, 0), Size(10, 10), 1, Direction.UP),
                [
                    Entity("2", Vector(0, 13), Size(10, 10)),
                    Entity("3", Vector(0, 14), Size(10, 10)),
                ],
                Entity("2", Vector(0, 13), Size(10, 10)),
                Vector(1, 2),
            ),
            (
                Movable("1", Vector(10, 15), Size(10, 10), 1, Direction.DOWN),
                [
                    Entity("2", Vector(3, 1), Size(10, 10)),
                    Entity("3", Vector(14, 2), Size(10, 10)),
                ],
                Entity("3", Vector(14, 2), Size(10, 10)),
                Vector(10, 13),
            ),
            (
                Movable("1", Vector(1, 0), Size(10, 10), 1, Direction.RIGHT),
                [
                    Entity("2", Vector(15, 3), Size(10, 1)),
                    Entity("3", Vector(13, 2), Size(10, 1)),
                ],
                Entity("3", Vector(13, 2), Size(10, 1)),
                Vector(2, 0),
            ),
            (
                Movable("1", Vector(15, 0), Size(10, 10), 1, Direction.LEFT),
                [
                    Entity("2", Vector(1, 2), Size(10, 1)),
                    Entity("3", Vector(2, 3), Size(10, 1)),
                ],
                Entity("3", Vector(2, 3), Size(10, 1)),
                Vector(13, 0),
            ),
        ],
    )
    def test__resolve_conflicts_with_other_entities(
        self, entity, entities, expected_entity, expected_position
    ):
        actual = Movable._resolve_conflicts_with_other_entities(entity, entities)

        assert entity.position == expected_position
        assert actual == expected_entity

    @pytest.mark.parametrize(
        "position,size,direction,new_position,expected_params",
        [
            (
                Vector(0, 0),
                Size(1, 1),
                Direction.UP,
                Vector(0, 2),
                [Vector(0, 0), Size(1, 3)],
            ),
            (
                Vector(4, 0),
                Size(1, 1),
                Direction.LEFT,
                Vector(2, 0),
                [Vector(2, 0), Size(3, 1)],
            ),
            (
                Vector(0, 0),
                Size(1, 1),
                Direction.RIGHT,
                Vector(2, 0),
                [Vector(0, 0), Size(3, 1)],
            ),
            (
                Vector(0, 4),
                Size(1, 1),
                Direction.DOWN,
                Vector(0, 2),
                [Vector(0, 2), Size(1, 3)],
            ),
        ],
    )
    def test__get_conflict_entities(
        self, position, size, direction, new_position, expected_params
    ):
        map_ = MagicMock()
        entity_obj = MagicMock(position=position, size=size, direction=direction)

        Movable._get_conflict_entities(entity_obj, new_position, map_)

        map_.get_entities_by_location.assert_called_once_with(*expected_params)
