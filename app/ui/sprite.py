from typing import Union

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap, QWindow
from PyQt5.QtWidgets import QLabel

from app.domain.entities.interfaces import Entity, Moveable

BASIC_TRANSITION = 8


class Sprite(QLabel):
    def __init__(
        self, parent_frame: QWindow, entity: Union[Entity, Moveable], path_to_image: str
    ):
        super().__init__(parent_frame)
        self.entity = entity
        self.resize(
            BASIC_TRANSITION * self.entity.size.width,
            BASIC_TRANSITION * self.entity.size.height,
        )
        self.move(
            BASIC_TRANSITION * self.entity.location.x,
            BASIC_TRANSITION * self.entity.location.y,
        )
        self._display_image(path_to_image)

    def _display_image(self, path_to_image: str) -> None:
        pixmap = QPixmap(path_to_image)
        self.resize(pixmap.width(), pixmap.height())
        self.setPixmap(pixmap)

    def move_sprite(self) -> None:
        self.move(
            QPoint(
                BASIC_TRANSITION * self.entity.location.x,
                BASIC_TRANSITION * self.entity.location.y,
            )
        )
