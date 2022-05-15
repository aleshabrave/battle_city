from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QImage

from app.domain.entities.interfaces import Entity
from app.ui.paths_to_images import PATHS_TO_IMAGES


class Sprite:
    def __init__(self, entity: Entity, basic_transition: int = 8):
        self._entity = entity
        self._image = QImage(PATHS_TO_IMAGES[entity.name])
        self._basic_transition = basic_transition

    @property
    def next_image(self) -> QImage:
        return self._image

    @property
    def coordinates(self) -> QPoint:
        return QPoint(
            self._basic_transition * self._entity.location.x,
            self._basic_transition * self._entity.location.y,
        )
