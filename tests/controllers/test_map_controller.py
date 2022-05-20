from unittest.mock import MagicMock, MagicProxy

import pytest

from app.controllers.map_controller import MapController
from app.domain.entities.interfaces import Entity, Living, MovableEntity


class TestsMapController:
    def test__update_map(self):
        controller = MagicMock()

        map_ = MapController.update_map(controller)

        controller._move_entities.assert_called_once_with()
        assert map_ == controller._map

    def test__move_entities(self):
        parents = [MovableEntity, Living, Entity]
        entities = [MagicMock(__class__=parent) for parent in parents]
        map_ = MagicMock()
        controller = MapController(_map=map_)
        controller._map.get_entities.return_value = entities

        controller._move_entities()

        controller._map.get_entities.assert_called_once_with()
        for entity in filter(lambda x: isinstance(x, MovableEntity), entities):
            entity.update_location.assert_called_once_with(map_)
