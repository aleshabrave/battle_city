from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QStackedWidget

from app.constants import Default
from app.controllers import GameController
from app.levels.generator import GameGenerator
from app.ui.widgets.entry import EntryWidget
from app.ui.widgets.game import GameWidget
from app.ui.widgets.menu import MenuWidget


class MainWindow(QMainWindow):
    username: str = None
    new_game_flag: bool = True
    game_controller: GameController = None

    def __init__(self, size: QSize, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Battle city")
        self.setWindowIcon(QIcon(Default.PATH_TO_ICON))
        self.setFixedSize(size)

        self.widgets = QStackedWidget(self)
        self.initWidgets(size)

        self.display(0)

    def initWidgets(self, size: QSize):
        self.widgets.resize(size)
        entry = EntryWidget(self)
        menu = MenuWidget(self)
        game = GameWidget(self, 0.1)

        self.widgets.addWidget(entry)
        self.widgets.addWidget(menu)
        self.widgets.addWidget(game)

    def display(self, idx: int):
        self.widgets.setCurrentIndex(idx)
        self.widgets.currentWidget().init()
