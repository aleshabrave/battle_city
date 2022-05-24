from PyQt5.QtCore import QRect
from PyQt5.QtGui import QKeyEvent, QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget

from app.controllers import GameController
from app.domain.interfaces import Entity
from app.ui.sprite import Sprite


class GameWidget:
    def __init__(self, window: QMainWindow, widget: QWidget, game_controller: GameController):
        self.window = window
        self.widget = widget
        self.widget.setStyleSheet("background-color: black;")
        self._init_sprites()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self.game_controller.player_controller.handle_press_key(event)

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        self.game_controller.player_controller.handle_release_key(event)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        for entity in self.game_controller.get_current_level().map_.entities:
            sprite = self._get_else_create_sprite(entity)
            painter.drawImage(sprite.coordinates, sprite.next_image)
        self._delete_old_sprites()

    def _init_sprites(self) -> None:
        self._sprites: dict[Entity, Sprite] = dict()
        for entity in self.game_controller.get_current_level().map_.entities:
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
        for entity in self.game_controller.get_current_level().map_.entities:
            new[entity] = self._sprites[entity]
        self._sprites = new
