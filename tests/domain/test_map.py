from unittest.mock import MagicMock

import pytest

from app.domain.data import Size, Vector
from app.domain.entities.interfaces import Entity
from app.domain.map import Map
from tests import data


class TestsMap:
    def test__get_entities(self):
        entities = (
            self._get_entity("aboba"),
            self._get_entity("aboba"),
            self._get_entity("amogus"),
        )
        map_ = Map(MagicMock(), {})
        data._set_up_map(map_, entities)

        actual = map_.get_entities()

        assert actual == set(entities)
        assert len(map_._entities) != 0

    def test__get_entities_by_name(self):
        entities = (
            self._get_entity("aboba"),
            self._get_entity("aboba"),
            self._get_entity("amogus"),
        )
        self._check_get_entities_by_name(entities, "aboba", set(entities[:2]))

    def test__get_entities_by_name_if_no_needed_name(self):
        entities = (self._get_entity("aboba"),)
        self._check_get_entities_by_name(entities, "amogus", None)

    def _check_get_entities_by_name(self, entities, name, expected):
        map_ = Map(MagicMock(), {})
        data._set_up_map(map_, entities)

        actual = map_.get_entities_by_name(name)

        assert actual == expected
        assert len(map_._entities) != 0

    def test__get_entities_by_location_if_no_entities(self):
        entities = (
            self._get_entity("test_name1", location=Vector(0, 0), size=Size(1, 1)),
            self._get_entity("test_name2", location=Vector(3, 3), size=Size(1, 1)),
        )
        point = Vector(2, 2)
        self._check_get_entities_by_location(entities, point, None)

    def test__get_entities_by_location_if_some_entities(self):
        entities = (
            self._get_entity("test_name1", location=Vector(0, 0), size=Size(1, 1)),
            self._get_entity("test_name2", location=Vector(1, 1), size=Size(1, 1)),
        )
        point = Vector(1, 1)
        self._check_get_entities_by_location(entities, point, set(entities))

    def test__get_entities_by_location_if_one_entity(self):
        entities = (
            self._get_entity("test_name1", location=Vector(0, 0), size=Size(1, 1)),
            self._get_entity("test_name2", location=Vector(3, 3), size=Size(1, 1)),
        )
        point = Vector(1, 1)
        self._check_get_entities_by_location(entities, point, set(entities[:1]))

    def _check_get_entities_by_location(self, entities, point, expected):
        map_ = Map(MagicMock(), {})
        data._set_up_map(map_, entities)

        actual = map_.get_entities_by_location(point)

        assert actual == expected

    def test__get_neighbours_if_no_neighbours(self):
        entity = self._get_entity("test_name3", location=Vector(1, 1), size=Size(1, 1))
        entities = [
            self._get_entity("test_name1", location=Vector(0, 0), size=Size(1, 1)),
            self._get_entity("test_name2", location=Vector(2, 2), size=Size(1, 1)),
            entity,
        ]
        self._check_get_neighbours(entities, entity, None)

    def test__get_neighbours_if_some_neighbours(self):
        entity = self._get_entity("test_name3", location=Vector(1, 1), size=Size(1, 1))
        entities = [
            self._get_entity("test_name1", location=Vector(1, 1), size=Size(1, 1)),
            self._get_entity("test_name2", location=Vector(1, 1), size=Size(1, 1)),
            entity,
        ]
        self._check_get_neighbours(entities, entity, set(entities[:2]))

    def test__get_neighbours_if_one_neighbour(self):
        entity = self._get_entity("test_name3", location=Vector(1, 1), size=Size(1, 1))
        entities = [
            self._get_entity("test_name1", location=Vector(0, 0), size=Size(1, 1)),
            self._get_entity("test_name2", location=Vector(1, 1), size=Size(1, 1)),
            entity,
        ]
        self._check_get_neighbours(entities, entity, set(entities[1:2]))

    def _check_get_neighbours(self, entities, entity, expected):
        map_ = Map(MagicMock(), {})
        data._set_up_map(map_, entities)

        actual = map_.get_neighbours(entity)

        assert actual == expected

    @pytest.mark.parametrize(
        "location,entity_size,map_size,expected",
        [
            (Vector(-1, 0), Size(1, 1), Size(1, 1), True),
            (Vector(1, 0), Size(1, 1), Size(1, 1), True),
            (Vector(0, 1), Size(1, 1), Size(1, 1), True),
            (Vector(0, -1), Size(1, 1), Size(1, 1), True),
            (Vector(0, 0), Size(1, 1), Size(1, 1), False),
            (Vector(5, 5), Size(1, 1), Size(10, 10), False),
        ],
    )
    def test__check_out_of_bounds(self, location, entity_size, map_size, expected):
        entity = self._get_entity("test_name", location, entity_size)
        map_ = Map(map_size, {})
        data._set_up_map(map_, (entity,))

        actual = map_.check_out_of_bounds(entity)

        assert actual == expected
        assert len(map_._entities) != 0

    def test__add_entity(self):
        entity = self._get_entity("aboba")
        map_ = Map(MagicMock(), {})

        map_.add_entity(entity)

        assert len(map_._entities) == 1
        assert entity.name in map_._entities
        assert entity in map_._entities[entity.name]

    def test__remove_entity(self):
        entity = self._get_entity("aboba")
        map_ = Map(MagicMock(), {entity.name: {entity}})

        map_.remove_entity(entity)

        assert len(map_._entities) == 0

    @staticmethod
    def _get_entity(name, location=None, size=None):
        return Entity(name, location, size)
