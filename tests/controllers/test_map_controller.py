from unittest.mock import MagicMock

from app.controllers.map_controller import MapController
from app.domain.interfaces import Entity, Living, Movable
from app.domain.map import Map


class TestsMapController:
    def test__update_map(self):
        clss = [Movable, Living, Entity]
        map_ = Map(
            size=MagicMock(), entities=[MagicMock(spec=parent) for parent in clss]
        )
        controller = MapController(map_=map_)

        controller.update_map()

        for entity in filter(lambda x: isinstance(x, Movable), map_.entities):
            entity.update_location.assert_called_once_with(map_)
