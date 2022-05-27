from dataclasses import dataclass
from sys import argv, exit
from threading import Thread
from time import sleep

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication

from app.controllers.game_controller import GameController
from app.ui.main_window import MainWindow


@dataclass
class MainLoop:
    _game_controller: GameController
    _tick_duration_secs: float
    _window_size: QRect
    _main_window: MainWindow = None

    def start(self):
        app = QApplication(argv)
        self._game_controller.init_game()
        self._main_window = MainWindow(
            self._game_controller,
            self._window_size,
        )
        self._main_window.show()
        Thread(target=self._main).start()
        exit(app.exec_())

    def _main(self) -> None:
        self._game_controller.run()
        while True:
            sleep(self._tick_duration_secs)
            self._main_window.update()
