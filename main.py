import sys
from time import sleep
import threading

from PyQt5.QtWidgets import QApplication

from app.controllers.map_controller import MapController
from app.levels import parser
from app.ui.ui import UI


# class MyApp(QApplication):
#     def __init__(self, *args, **kwargs):
#         super().

def method_name(map_controller, ui: UI):
    while True:
        # ui.show_entities(map_controller)
        sleep(2)
        map_controller.move_entities()
        # ui.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    map_controller = MapController(parser.parse_map("./levels/wall_level.txt"))
    ui = UI(map_controller)
    threading.Thread(target=method_name, args=(map_controller, ui)).start()
    sys.exit(app.exec_())
