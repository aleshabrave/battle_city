import math

from PyQt5.QtCore import QPoint, QRect, QSize
from PyQt5.QtGui import QImage, QTransform

from app.domain.enums import Direction
from app.domain.interfaces import Entity, Movable
from app.ui.images import Images


class Sprite:
    """Class for work with sprites."""

    def __init__(self, entity: Entity, basic_transition: int = 2):
        self._entity = entity
        self._init_images()
        self._basic_transition = basic_transition

    def next_image(self, shift_flag=True) -> QImage:
        """Next image for animation."""
        image = self._images[self._number_of_current_image]
        if (
            isinstance(self._entity, Movable)
            and self._entity.is_moving()
            and shift_flag
        ):
            self._shift_number_of_current_image()
        return image.transformed(self._get_rotation_angle())

    @property
    def coordinates(self) -> QRect:
        """Coordinates."""
        return QRect(
            QPoint(self._entity.position.x, self._entity.position.y)
            * self._basic_transition,
            QSize(self._entity.size.width, self._entity.size.height)
            * self._basic_transition,
        )

    def _init_images(self) -> None:
        """Initialize images."""
        self._images: list[QImage] = Images.get_images(self._entity.name)
        self._count_of_images = len(self._images)
        self._number_of_current_image = 0

    def _get_rotation_angle(self) -> QTransform:
        """Get new angle."""
        angle = (
            math.degrees(self._entity.direction.value + Direction.UP.value)
            if isinstance(self._entity, Movable)
            else 0
        )
        return QTransform().rotate(angle)

    def _shift_number_of_current_image(self) -> None:
        """Shift animation image index."""
        self._number_of_current_image += 1
        self._number_of_current_image %= self._count_of_images
