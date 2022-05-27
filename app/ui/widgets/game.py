import time
from threading import Thread
from typing import TYPE_CHECKING

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QKeyEvent, QPainter
from PyQt5.QtWidgets import QBoxLayout, QPushButton, QFrame, QLabel

from app.constants import Default
from app.domain.interfaces import Entity
from app.ui.sprite import Sprite

if TYPE_CHECKING:
    from app.ui.main_window import MainWindow


class GameWidget(QFrame):
    def __init__(self, parent: "MainWindow"):
        super(GameWidget, self).__init__(parent)
        self.main_window = parent

        self.game_status_label = QLabel(self)
        self.game_status_label.setStyleSheet("QLabel { color : green; }")
        self.level_status_label = QLabel(self)
        self.level_status_label.setStyleSheet("QLabel { color : green; }")
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
        layout.addWidget(self.game_status_label)
        layout.addWidget(self.level_status_label)

        layout.setGeometry(QRect(392, 0, 120, 100))

        pause_button.clicked.connect(self.pauseButtonClicked)
        restart_button.clicked.connect(self.restartButtonClicked)
        save_button.clicked.connect(self.saveButtonClicked)

    def init(self):
        self.setStyleSheet("background-color: black;")
        self.main_window.game_controller.init_game(
            new_game_flag=self.main_window.new_game_flag
        )
        Thread(target=self.main_window.game_controller.run).start()
        Thread(target=self.updateStatuses).start()
        self._init_sprites()

    def updateStatuses(self):
        while True:
            time.sleep(1)
            self.game_status_label.setText(
                f"Game status is {self.main_window.game_controller.game.state.value}"
            )
            self.game_status_label.adjustSize()
            self.level_status_label.setText(
                f"Level status is {self.main_window.game_controller.get_current_level().state.value}"
            )

    def pauseButtonClicked(self):
        self.main_window.game_controller.pause = (
            not self.main_window.game_controller.pause
        )

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
        painter = QPainter(self)
        for (
            entity
        ) in self.main_window.game_controller.get_current_level().map_.entities:
            sprite = self._get_else_create_sprite(entity)
            painter.drawImage(sprite.coordinates, sprite.next_image)
        # self._delete_old_sprites()
        self.update()

    def _init_sprites(self) -> None:
        self._sprites: dict[Entity, Sprite] = dict()
        for (
            entity
        ) in self.main_window.game_controller.get_current_level().map_.entities:
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
        for (
            entity
        ) in self.main_window.game_controller.get_current_level().map_.entities:
            new[entity] = self._sprites[entity]
        self._sprites = new
