from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QMessageBox

from app.constants import Default
from app.controllers import GameController
from app.ui.widgets.entry import EntryWidget
from app.ui.widgets.game import GameWidget
from app.ui.widgets.menu import MenuWidget


class MainWindow(QMainWindow):
    username: str = None
    new_game_flag: bool = True
    game_controller: GameController = None

    def __init__(self, size: QSize = QSize(612, 512), parent=None):
        super().__init__(parent)
        self.setWindowTitle("WORLD OF TANKS")
        self.setWindowIcon(QIcon(Default.PATH_TO_ICON))
        self.setFixedSize(size)

        self.entry = EntryWidget(self)
        self.menu = MenuWidget(self)
        self.game = GameWidget(self)
        self.widgets = QStackedWidget(self)
        self.initWidgets(size)

        self.display(0)

    def initWidgets(self, size: QSize):
        self.widgets.resize(size)
        self.widgets.addWidget(self.entry)
        self.widgets.addWidget(self.menu)
        self.widgets.addWidget(self.game)

    def display(self, idx: int):
        self.widgets.setCurrentIndex(idx)
        self.widgets.currentWidget().init()

    def closeEvent(self, e):
        if self.game_controller is None or self.game_controller.game is None:
            e.accept()
            return

        self.game_controller.pause.set()

        result = QMessageBox.question(
            self,
            "Accept closing WORLD OF TANKS",
            "Maybe save?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)

        if result == QMessageBox.Yes:
            self.game_controller.save()

        self.game.close()
        e.accept()
        QMainWindow.closeEvent(self, e)

