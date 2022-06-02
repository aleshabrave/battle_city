import time
from threading import Thread
from typing import TYPE_CHECKING

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QKeyEvent, QPainter
from PyQt5.QtWidgets import QBoxLayout, QFrame, QLabel, QPushButton

from app.constants import Default
from app.controllers import GameController
from app.domain.interfaces import Entity
from app.ui.sprite import Sprite

if TYPE_CHECKING:
    from app.ui.main_window import MainWindow


class GameWidget(QFrame):
    def __init__(self, parent: "MainWindow"):
        super(GameWidget, self).__init__(parent)

        self.main_window = parent

        self.status_handler = Thread(target=self.updateStatuses)
        self.status_handler_stop_flag = False

        self.game_status_label = QLabel(self)
        self.game_status_label.setStyleSheet("QLabel { color : green; }")

        pause_button = QPushButton(Default.PAUSE_BUTTON, self)
        pause_button.setStyleSheet(f"background-color: green;")
        pause_button.setFocusPolicy(Qt.NoFocus)
        restart_button = QPushButton(Default.RESTART_BUTTON, self)
        restart_button.setStyleSheet(f"background-color: green;")
        restart_button.setFocusPolicy(Qt.NoFocus)
        save_button = QPushButton(Default.SAVE_BUTTON, self)
        save_button.setStyleSheet(f"background-color: green;")
        save_button.setFocusPolicy(Qt.NoFocus)

        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
        layout.addWidget(pause_button)
        layout.addWidget(restart_button)
        layout.addWidget(save_button)
        layout.addWidget(self.game_status_label)
        layout.setGeometry(QRect(512, 0, 100, 100))

        pause_button.clicked.connect(self.pauseButtonClicked)
        restart_button.clicked.connect(self.restartButtonClicked)
        save_button.clicked.connect(self.saveButtonClicked)

    def init(self):
        self.setStyleSheet("background-color: black;")
        self.main_window.game_controller.init_game(
            player_fabric=self.main_window.player_fabric,
            new_game_flag=self.main_window.new_game_flag,
        )

        self.main_window.game_controller.start()
        self.status_handler.start()

        self._init_sprites()

    def updateStatuses(self):
        while not self.status_handler_stop_flag:
            time.sleep(1)
            self.game_status_label.setText(
                f"Game status is "
                f"{self.main_window.game_controller.game.state.value}"
                f"\nhp:"
                f" {self.main_window.game_controller.player_controller.tank_controller.tank.health_points}"
                f"\nbullet damage: "
                f"{self.main_window.game_controller.player_controller.tank_controller.tank._bullet_schema.damage}"
                f"\nbullet speed: "
                f"{self.main_window.game_controller.player_controller.tank_controller.tank._bullet_schema.speed}"
            )
            self.game_status_label.adjustSize()

    def pauseButtonClicked(self):
        if self.main_window.game_controller.pause.is_set():
            self.main_window.game_controller.pause.clear()
        else:
            self.main_window.game_controller.pause.set()

    def restartButtonClicked(self):
        self.main_window.game_controller.stop = True
        self.main_window.game_controller.join()
        self.main_window.game_controller = GameController.create(
            timer=self.main_window.game_controller.timer,
            username=self.main_window.username,
            new_game_flag=True,
            player_fabric=self.main_window.player_fabric,
        )
        self.main_window.game_controller.start()

    def saveButtonClicked(self):
        self.main_window.game_controller.save()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if self.main_window.game_controller.pause.is_set():
            return
        self.main_window.game_controller.player_controller.handle_press_key(event)

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        if self.main_window.game_controller.pause.is_set():
            return
        self.main_window.game_controller.player_controller.handle_release_key(event)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        for entity in self.main_window.game_controller.map_controller.map_.entities:
            sprite = self._get_else_create_sprite(entity)
            painter.drawImage(sprite.coordinates, sprite.next_image)
        # self._delete_old_sprites()
        self.update()

    def _init_sprites(self) -> None:
        self._sprites: dict[Entity, Sprite] = dict()
        for entity in self.main_window.game_controller.map_controller.map_.entities:
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
        for entity in self.main_window.game_controller.map_controller.map_.entities:
            new[entity] = self._sprites[entity]
        self._sprites = new

    def close(self):
        self.status_handler_stop_flag = True
        self.main_window.game_controller.stop = True

        self.main_window.game_controller.join()
        self.status_handler.join()
