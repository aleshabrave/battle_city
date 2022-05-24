from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QWidget

from app.constants import Default
from app.ui.widgets.menu import MenuWidget


class MainWindow(QMainWindow):
    def __init__(self, size: QSize, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Battle city")
        self.setWindowIcon(QIcon(Default.PATH_TO_ICON))
        self.setFixedSize(size)

        self.widgets = QStackedWidget(self)
        self.initWidgets(size)

    def initWidgets(self, size):
        self.widgets.resize(size)
        menu = MenuWidget(self, QWidget())
        self.widgets.addWidget(menu.widget)

    def display(self, idx: int):
        self.widgets.setCurrentIndex(idx)
