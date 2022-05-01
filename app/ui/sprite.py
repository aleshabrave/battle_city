from typing import Union

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap, QWindow
from PyQt5.QtWidgets import QLabel

from app.domain.entities.interfaces import Entity, Moveable


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
