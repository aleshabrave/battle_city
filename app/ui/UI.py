from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtWidgets import QMainWindow

from app.controllers.map_controller import MapController
from app.domain.entities.interfaces import Entity
from app.ui.paths_to_images import PATHS_TO_IMAGES
from app.ui.sprite import Sprite

_BASIC_TRANSITION = 8


class UI(QMainWindow):
    def __init__(self, map_controller: MapController, size: QRect):
        super().__init__()
        self._map_controller = map_controller
        self._init_sprites()
        self.setGeometry(size)
        self.setStyleSheet("background-color: black;")
        self.show()

    def _init_sprites(self):
        self._sprites: dict[Entity, Sprite] = dict()
        for entity in self._map_controller.map.entities:
            self._sprites[entity] = Sprite(entity)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        for entity in self._map_controller.map.entities:
            try:
                sprite = self._sprites[entity]
            except KeyError:
                self._sprites[entity] = Sprite(entity)
                sprite = self._sprites[entity]
            painter.drawImage(sprite.coordinates, sprite.next_image)
