import sys
import threading
from time import sleep

from PyQt5.QtWidgets import QApplication

from app.controllers.map_controller import MapController
from app.levels import parser
from app.ui.ui import UI


def move_spites() -> None:
    while True:
        sleep(0.5)
        ui.move_spites()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    map_controller = MapController(parser.parse_map("./levels/wall_level.txt"))
    ui = UI(map_controller)
    threading.Thread(target=move_spites).start()
    sys.exit(app.exec_())
