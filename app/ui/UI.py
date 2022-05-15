from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtWidgets import QMainWindow

from app.controllers.map_controller import MapController
from app.domain.entities.interfaces import Entity
from app.ui.paths_to_images import PATHS_TO_IMAGES

_BASIC_TRANSITION = 8


class UI(QMainWindow):
    def __init__(self, map_controller: MapController, size: QRect):
        super().__init__()
        self._map_controller = map_controller
        self.setGeometry(size)
        self.setStyleSheet("background-color: black;")
        self.show()

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        for entity in self._map_controller.map.entities:
            coords = self._convert_entity_location_to_rendering_coordinates(entity)
            painter.drawImage(coords, QImage(PATHS_TO_IMAGES[entity.name]))

    @staticmethod
    def _convert_entity_location_to_rendering_coordinates(entity: Entity) -> QPoint:
        return QPoint(
            _BASIC_TRANSITION * entity.location.x,
            _BASIC_TRANSITION * entity.location.y,
        )
