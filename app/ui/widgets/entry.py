from typing import TYPE_CHECKING

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QBoxLayout, QLabel, QLineEdit, QPushButton, QWidget

from app.constants import Default
from app.controllers import GameController
from app.levels.generator import GameGenerator

if TYPE_CHECKING:
    from app.ui.main_window import MainWindow


class EntryWidget(QWidget):
    def __init__(self, parent: "MainWindow"):
        super(EntryWidget, self).__init__(parent)
        self.main_window = parent

        self.label = QLabel(self)
        self.entry_label = QLabel(self)
        self.entry_label.setText("Введите никнейм:")
        self.entry_label.setStyleSheet("QLabel { color : green; }")

        qle = QLineEdit(self)
        qle.setStyleSheet(f"background-color: green;")
        qle.resize(100, 100)
        go_button = QPushButton(Default.GO_BUTTON, self)
        go_button.setStyleSheet(f"background-color: green;")

        qle.textChanged[str].connect(self.onChanged)
        go_button.clicked.connect(self.goButtonClicked)

        layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        layout.addWidget(qle)
        layout.addWidget(go_button)
        layout.setGeometry(QRect(156, 200, 200, 100))

    def init(self):
        self.main_window.setStyleSheet("background-color: black;")

    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()

    def goButtonClicked(self):
        text = self.label.text()
        if len(text) == 0:
            return
        self.main_window.username = text
        self.main_window.game_controller = GameController(
            0.1, GameGenerator(text)
        )
        self.main_window.display(1)
