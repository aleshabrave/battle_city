import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QApplication,
)


def main():
    app = QApplication(sys.argv)
    win = MainWindow(QSize(512, 512))
    win.show()
    sys.exit(app.exec_())

    # with migration.on_app_start():
    #     game_generator = GameGenerator("lol")
    #     game_controller = GameController(0.1, game_generator)
    #
    #     MainLoop(game_controller, 0.1, QRect(QPoint(0, 0), QPoint(512, 512))).start()


if __name__ == "__main__":
    main()
