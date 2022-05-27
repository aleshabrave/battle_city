from typing import TYPE_CHECKING

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QBoxLayout, QLabel, QPushButton, QWidget

from app.constants import Default
from app.controllers import GameController
from app.levels.generator import GameGenerator

if TYPE_CHECKING:
    from app.ui.main_window import MainWindow


class MenuWidget(QWidget):
    def __init__(self, parent: "MainWindow"):
        super(MenuWidget, self).__init__(parent)
        self.main_window = parent

        self.hello_label = QLabel(self)

        new_game_button = QPushButton(Default.NEW_GAME_BUTTON_NAME, self)
        new_game_button.setStyleSheet(f"background-color: green;")
        continue_game_button = QPushButton(Default.CONTINUE_GAME_BUTTON_NAME, self)
        continue_game_button.setStyleSheet(f"background-color: green;")

        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
        layout.addWidget(self.hello_label)
        layout.addWidget(new_game_button)
        layout.addWidget(continue_game_button)

        layout.setGeometry(QRect(206, 250, 100, 150))

        new_game_button.clicked.connect(self.newGameButtonClicked)
        continue_game_button.clicked.connect(self.continueGameButtonClicked)

    def init(self):
        self.hello_label.setText(f"Привет, {self.main_window.username}!")
        self.hello_label.setStyleSheet("QLabel { color : green; }")
        self.hello_label.resize(512, 50)
        self.hello_label.setFont(QFont("Arial", 10))

    def newGameButtonClicked(self):
        self.main_window.new_game_flag = True
        self.main_window.display(2)

    def continueGameButtonClicked(self):
        self.main_window.new_game_flag = False
        self.main_window.display(2)
