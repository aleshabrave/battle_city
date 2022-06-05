from unittest.mock import MagicMock

import pytest

from app.domain.exceptions import MapException
from app.domain.interfaces import Entity
from app.domain.map import Map
from app.domain.utils import Size, Vector


class TestsMap:
    @pytest.mark.parametrize(
        "entities,expected",
        [([Entity("1", None, None)], [Entity("1", None, None)]), (None, [])],
    )
    def test__post_init(self, entities, expected):
        map_ = Map(size=MagicMock(), entities=entities)

        assert map_.entities == expected

    def test__get_player_tank(self):
        player = MagicMock()
        player.name = "player_tank"
        some_entity = MagicMock()
        some_entity.name = "some_entity"
        map_ = Map(size=MagicMock(), entities=[player, some_entity])

        actual = map_.get_player_tank()

        assert actual == player

    @pytest.mark.parametrize(
        "players,message",
        [
            ([MagicMock(), MagicMock()], "Too many players, but should be only one."),
            ([], "No player."),
        ],
    )
    def test__get_player_tank_with_exception(self, players, message):
        for player in players:
            player.name = "player_tank"
        map_ = Map(size=MagicMock(), entities=players)

        with pytest.raises(MapException, match=message):
            map_.get_player_tank()

    def test__get_enemy_tanks(self):
        tank1 = MagicMock()
        tank1.name = "enemy_tank_1"
        tank2 = MagicMock()
        tank2.name = "enemy_tank_2"
        some_entity = MagicMock()
        some_entity.name = "some_entity"
        map_ = Map(size=MagicMock(), entities=[tank1, tank2, some_entity])

        actual = map_.get_enemy_tanks()

        assert actual == [tank1, tank2]

    @pytest.mark.parametrize(
        "name,entities,expected",
        [
            (
                "1",
                [Entity("1", None, None), Entity("1", None, None)],
                [Entity("1", None, None), Entity("1", None, None)],
            ),
            ("1", [Entity("2", None, None), Entity("2", None, None)], []),
        ],
    )
    def test__get_entities_by_name(self, name, entities, expected):
        map_ = Map(size=MagicMock(), entities=entities)

        actual = map_.get_entities_by_name(name)

        assert actual == expected

    @pytest.mark.parametrize(
        "entities,position,size,expected",
        [
            (
                [
                    Entity("1", Vector(0, 0), Size(1, 1)),
                    Entity("2", Vector(1, 1), Size(1, 1)),
                ],
                Vector(0, 0),
                Size(2, 2),
                [
                    Entity("1", Vector(0, 0), Size(1, 1)),
                    Entity("2", Vector(1, 1), Size(1, 1)),
                ],
            ),
            (
                [
                    Entity("1", Vector(0, 0), Size(1, 1)),
                    Entity("2", Vector(1, 1), Size(1, 1)),
                ],
                Vector(2, 2),
                Size(2, 2),
                [],
            ),
            (
                [
                    Entity("1", Vector(0, 0), Size(2, 2)),
                    Entity("2", Vector(1, 1), Size(1, 1)),
                ],
                Vector(0, 0),
                Size(1, 1),
                [Entity("1", Vector(0, 0), Size(2, 2))],
            ),
        ],
    )
    def test__get_entities_by_location(self, entities, position, size, expected):
        map_ = Map(size=MagicMock())
        map_.entities = entities
        actual = map_.get_entities_by_location(position, size)

        assert actual == expected

    @pytest.mark.parametrize(
        "position,size,map_size,expected",
        [
            (Vector(-1, 0), Size(1, 1), Size(1, 1), True),
            (Vector(1, 0), Size(1, 1), Size(1, 1), True),
            (Vector(0, 1), Size(1, 1), Size(1, 1), True),
            (Vector(0, -1), Size(1, 1), Size(1, 1), True),
            (Vector(0, 0), Size(1, 1), Size(1, 1), False),
            (Vector(5, 5), Size(1, 1), Size(10, 10), False),
        ],
    )
    def test__check_out_of_bounds(self, position, size, map_size, expected):
        map_ = Map(map_size)

        actual = map_.check_out_of_bounds(position, size)

        assert actual == expected

    def test__add_entity(self):
        entity = Entity("1", None, None)
        map_ = Map(size=MagicMock())

        map_.add_entity(entity)

        assert entity in map_.entities
        assert len(map_.entities) == 1

    def test__remove_entity(self):
        entity = Entity("1", None, None)
        map_ = Map(size=MagicMock(), entities=[entity])

        map_.remove_entity(entity)

        assert entity not in map_.entities
