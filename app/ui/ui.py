from time import sleep
from typing import Union

from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QPixmap, QWindow
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QMainWindow

from app.controllers.map_controller import MapController
from app.domain.entities.interfaces import Entity, Moveable

PATHS_TO_IMAGES = {
    "default_tank": r".\app\ui\spites\tank.png",
    "default_wall": r".\app\ui\spites\wall.png",
}


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


class Sprite(QLabel):
    def __init__(
        self, parent_frame: QWindow, entity: Union[Entity, Moveable], path_to_image: str
    ):
        super().__init__(parent_frame)
        self.entity = entity
        self.resize(8 * self.entity.size.width, 8 * self.entity.size.height)
        self.move(8 * self.entity.location.x, 8 * self.entity.location.y)
        self._display_image(path_to_image)

    def _display_image(self, path_to_image: str) -> None:
        pixmap = QPixmap(path_to_image)
        self.resize(pixmap.width(), pixmap.height())
        self.setPixmap(pixmap)

    def move_sprite(self) -> None:
        loc = self.entity.location
        self.move(QPoint(8 * loc.x, 8 * loc.y))
