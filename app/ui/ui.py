from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QMainWindow

from app.controllers.map_controller import MapController

paths = {
    'default_tank': r'.\app\ui\spites\tank.png',
    'default_wall': r'.\app\ui\spites\wall.png'}


class UI(QMainWindow):

    def __init__(self, map_controller: MapController):
        super().__init__()

        self.setGeometry(0, 0, 720, 800)
        self._init_image()
        self._map_controller = map_controller
        self._labels = []
        self.show_entities(map_controller)
        self.show()
        self.update()

    def _init_image(self):
        self.layout = QHBoxLayout(self)
        self.layout.setGeometry(QRect(QPoint(0, 0), QPoint(700, 700)))
        self.setLayout(self.layout)

    def show_entities(self, map_controller):
        # for en in map_controller.map.entities:
        #     lbl = QLabel(self)
        #     self._labels.append(lbl)
        #     lbl.resize(
        #             8 * en.size.width,
        #             8 * en.size.height)
        #     lbl.move(
        #             8 * en.location.x,
        #             8 * en.location.y)
        #     self.layout.addWidget(lbl)
        #     self._display_image(paths[en.name], lbl)
        thank = None
        for en in map_controller.map.entities:
            if en.name == 'default_tank':
                thank = en
                break

        lbl = QLabel(self)
        self._labels.append(lbl)
        lbl.resize(
                8 * thank.size.width,
                8 * thank.size.height)
        lbl.move(
                8 * thank.location.x,
                8 * thank.location.y)
        self.layout.addWidget(lbl)
        self._display_image(paths[thank.name], lbl)

    def clear(self):
        for lbl in self._labels:
            lbl.clear()
        self._labels = []

    @staticmethod
    def _display_image(file_name, lbl):
        pixmap = QPixmap(file_name)  # .scaled(700, 700, Qt.KeepAspectRatio)
        lbl.resize(pixmap.width(), pixmap.height())
        lbl.setPixmap(pixmap)
