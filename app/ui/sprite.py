import math

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QImage, QTransform

from app.domain.data import Direction
from app.domain.entities.interfaces import Entity, Movable
from app.ui.paths_to_images import Images


class Sprite:
    def __init__(self, entity: Entity, basic_transition: int = 8):
        self._entity = entity
        self._init_images()
        self._basic_transition = basic_transition

    @property
    def next_image(self) -> QImage:
        image = self._images[self._number_of_current_image]
        self._shift_number_of_current_image()
        return image.transformed(self._get_rotation_angle())

    @property
    def coordinates(self) -> QPoint:
        return QPoint(
            self._basic_transition * self._entity.location.x,
            self._basic_transition * self._entity.location.y,
        )

    def _init_images(self) -> None:
        self._images: list[QImage] = Images.get_images(self._entity.name)
        self._count_of_images = len(self._images)
        self._number_of_current_image = 0

    def _get_rotation_angle(self) -> QTransform:
        angle = (
            0
            if not isinstance(self._entity, Movable)
            else math.degrees(self._entity.direction.value + Direction.UP.value)
        )
        return QTransform().rotate(angle)

    def _shift_number_of_current_image(self) -> None:
        self._number_of_current_image += 1
        self._number_of_current_image %= self._count_of_images
