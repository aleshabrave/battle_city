from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow

from app.controllers.map_controller import MapController
from app.ui.paths_to_images import PATHS_TO_IMAGES
from app.ui.sprite import Sprite


class UI(QMainWindow):
    def __init__(self, map_controller: MapController):
        super().__init__()
        self.setGeometry(QRect(QPoint(0, 0), QPoint(1000, 900)))
        self._init_layout()
        self._map_controller = map_controller
        self._sprites = []
        self._show_entities(map_controller)
        self.show()

    def _init_layout(self) -> None:
        self._layout = QHBoxLayout(self)
        self._layout.setGeometry(QRect(QPoint(0, 0), QPoint(1000, 900)))
        self.setLayout(self._layout)

    def _show_entities(self, map_controller) -> None:
        for en in map_controller.map.entities:
            sprite = Sprite(self, en, PATHS_TO_IMAGES[en.name])
            self._sprites.append(sprite)
            self._layout.addWidget(sprite)

    def move_spites(self) -> None:
        self._map_controller.move_entities()
        for sprite in self._sprites:
            sprite.move_sprite()
