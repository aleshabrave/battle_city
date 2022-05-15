from sys import argv, exit
from threading import Thread
from time import sleep

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication

from app.controllers.game_controller import GameController
from app.controllers.user_controller import UserController
from app.domain.data.enums import GameState
from app.ui.main_window import MainWindow


class MainLoop:
    def __init__(
        self,
        game_controller: GameController,
        tick_duration_secs: float,
        window_size: QRect,
    ):
        self._main_window = None
        self._game_controller = game_controller
        self._tick_duration_secs = tick_duration_secs
        self._window_size = window_size

    def start(self):
        app = QApplication(argv)
        self._main_window = MainWindow(
            self._game_controller.map_controller,
            UserController(self._game_controller.map_controller),
            self._window_size,
        )
        self._main_window.show()
        Thread(target=self._main).start()
        exit(app.exec_())

    def _main(self) -> None:
        while True:
            if self._game_controller.game_state == GameState.PAUSE:
                continue
            elif self._game_controller.game_state == GameState.FINISHED:
                # если победили, то подгружаем след уровень
                # если проиграли, то рестартим
                # но это обязанности кого-то другого нврн
                break
            sleep(self._tick_duration_secs)
            self._game_controller.map_controller.update_map()
            self._main_window.update()
