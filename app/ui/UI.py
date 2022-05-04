from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow

from app.controllers.map_controller import MapController
from app.ui.paths_to_images import PATHS_TO_IMAGES
from app.ui.sprite import Sprite


class UI(QMainWindow):
    def __init__(self, map_controller: MapController, size: QRect):
        super().__init__()
        self._map_controller = map_controller
        self._size = size
        self.setGeometry(self._size)
        self._init_graphic()
        self.show()

    def _init_graphic(self):
        self.setStyleSheet("background-color: black;")
        self._init_layout()
        self._sprites = []
        self._show_entities()

    def _init_layout(self) -> None:
        self._layout = QHBoxLayout(self)
        self._layout.setGeometry(self._size)
        self.setLayout(self._layout)

    def _show_entities(self) -> None:
        for en in self._map_controller.map.entities:
            sprite = Sprite(self, en, PATHS_TO_IMAGES[en.name])
            self._sprites.append(sprite)
            self._layout.addWidget(sprite)

    def move_spites(self) -> None:
        self._map_controller.move_entities()
        for sprite in self._sprites:
            sprite.move_sprite()
