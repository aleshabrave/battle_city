import time
from threading import Thread
from typing import TYPE_CHECKING

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QKeyEvent, QPainter
from PyQt5.QtWidgets import QBoxLayout, QPushButton, QWidget

from app.constants import Default
from app.controllers import GameController
from app.domain.interfaces import Entity
from app.levels.generator import GameGenerator
from app.ui.sprite import Sprite

if TYPE_CHECKING:
    from app.ui.main_window import MainWindow


class GameWidget(QWidget):
    def __init__(self, parent: "MainWindow", paint_timer: float):
        super(GameWidget, self).__init__(parent)
        self.main_window = parent
        self.paint_timer = paint_timer

        pause_button = QPushButton(Default.PAUSE_BUTTON, self)
        pause_button.setStyleSheet(f"background-color: green;")
        restart_button = QPushButton(Default.RESTART_BUTTON, self)
        restart_button.setStyleSheet(f"background-color: green;")
        save_button = QPushButton(Default.SAVE_BUTTON, self)
        save_button.setStyleSheet(f"background-color: green;")

        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
        layout.addWidget(pause_button)
        layout.addWidget(restart_button)
        layout.addWidget(save_button)

        layout.setGeometry(QRect(450, 0, 50, 150))

        pause_button.clicked.connect(self.pauseButtonClicked)
        restart_button.clicked.connect(self.restartButtonClicked)
        save_button.clicked.connect(self.saveButtonClicked)

    def init(self):
        self.setStyleSheet("background-color: black;")
        self.main_window.game_controller.init_game(new_game_flag=self.main_window.new_game_flag)
        Thread(target=self._start_game).start()
        self._init_sprites()

    def _start_game(self) -> None:
        self.main_window.game_controller.run()
        while True:
            time.sleep(self.paint_timer)
            self.update()

    def pauseButtonClicked(self):
        self.main_window.game_controller.pause = not self.game_controller.pause

    def restartButtonClicked(self):
        self.main_window.game_controller.init_game(new_game_flag=True)

    def saveButtonClicked(self):
        self.main_window.game_controller.save()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if self.main_window.game_controller.pause:
            return
        self.main_window.game_controller.player_controller.handle_press_key(event)

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        if self.main_window.game_controller.pause:
            return
        self.main_window.game_controller.player_controller.handle_release_key(event)

    def paintEvent(self, event) -> None:
        if self.main_window.game_controller.pause:
            return
        self.painter = QPainter(self)
        for entity in self.main_window.game_controller.get_current_level().map_.entities:
            sprite = self._get_else_create_sprite(entity)
            self.painter.drawImage(sprite.coordinates, sprite.next_image)
        self._delete_old_sprites()

    def _init_sprites(self) -> None:
        self._sprites: dict[Entity, Sprite] = dict()
        for entity in self.main_window.game_controller.get_current_level().map_.entities:
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
        for entity in self.main_window.game_controller.get_current_level().map_.entities:
            new[entity] = self._sprites[entity]
        self._sprites = new
