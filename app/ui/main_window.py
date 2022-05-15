from PyQt5.QtCore import QRect
from PyQt5.QtGui import QKeyEvent, QPainter
from PyQt5.QtWidgets import QMainWindow

from app.controllers.map_controller import MapController
from app.controllers.user_controller import UserController
from app.domain.entities.interfaces import Entity
from app.ui.sprite import Sprite


class MainWindow(QMainWindow):
    def __init__(
        self,
        map_controller: MapController,
        user_controller: UserController,
        size: QRect,
    ):
        super().__init__()
        self._map_controller = map_controller
        self._user_controller = user_controller
        self._init_sprites()
        self.setGeometry(size)
        self.setStyleSheet("background-color: black;")

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self._user_controller.handle_event(event)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        for entity in self._map_controller.map.entities:
            sprite = self._get_else_create_sprite(entity)
            painter.drawImage(sprite.coordinates, sprite.next_image)
        self._delete_old_sprites()

    def _init_sprites(self) -> None:
        self._sprites: dict[Entity, Sprite] = dict()
        for entity in self._map_controller.map.entities:
            self._sprites[entity] = Sprite(entity)

    def _get_else_create_sprite(self, entity: Entity) -> Sprite:
        try:
            sprite = self._sprites[entity]
        except KeyError:
            self._sprites[entity] = Sprite(entity)
            sprite = self._sprites[entity]
        return sprite

    def _delete_old_sprites(self) -> None:
        new: dict[Entity, Sprite] = dict()
        for entity in self._map_controller.map.entities:
            new[entity] = self._sprites[entity]
        self._sprites = new
