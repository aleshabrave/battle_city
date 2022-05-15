from sys import argv, exit
from threading import Thread
from time import sleep

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication

from app.controllers.game_controller import GameController
from app.domain.data.enums import GameState
from app.ui import UI


class MainLoop:
    def __init__(
        self,
        game_controller: GameController,
        tick_duration_secs: float,
        window_size: QRect,
    ):
        self._game_controller = game_controller
        self._tick_duration_secs = tick_duration_secs
        self._start_loop(window_size)

    def _start_loop(self, window_size):
        app = QApplication(argv)
        self._ui = UI.UI(self._game_controller.map_controller, window_size)
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
            self._ui.update()
