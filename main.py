from PyQt5.QtCore import QRect, QPoint

from app.controllers import GameController
from app.db import migration
from app.levels.generator import GameGenerator
from app.main_loop import MainLoop


def main():
    with migration.on_app_start():
        game_generator = GameGenerator("lol")
        game_controller = GameController(0.1, game_generator)

        MainLoop(game_controller, 0.1, QRect(QPoint(0, 0), QPoint(512, 512))).start()


if __name__ == "__main__":
    main()
