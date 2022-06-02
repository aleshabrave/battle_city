from typing import TYPE_CHECKING

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QBoxLayout, QLabel, QPushButton, QWidget

from app.constants import Default

if TYPE_CHECKING:
    from app.ui.main_window import MainWindow


class MenuWidget(QWidget):
    def __init__(self, parent: "MainWindow"):
        super(MenuWidget, self).__init__(parent)
        self.main_window = parent

        self.bg_label = QLabel(self)
        self.hello_label = QLabel(self)
        self.new_game_button = QPushButton(Default.NEW_GAME_BUTTON_NAME, self)
        self.continue_game_button = QPushButton(Default.CONTINUE_GAME_BUTTON_NAME, self)

        self.layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

    def init(self):
        self.bg_label.resize(612, 512)
        self.bg_label.setStyleSheet(
            f"background-image: url({Default.PATH_TO_MM_BACKGROUND});"
        )

        self.hello_label.setText(f"HELLO, {self.main_window.username}!")
        self.hello_label.setFont(QFont("Verdana", 12, QFont.Bold))
        self.hello_label.setStyleSheet("QLabel { color : white; }")

        self.new_game_button.clicked.connect(self.newGameButtonClicked)
        self.new_game_button.setFocusPolicy(Qt.NoFocus)

        self.continue_game_button.clicked.connect(self.continueGameButtonClicked)
        self.continue_game_button.setFocusPolicy(Qt.NoFocus)

        self.layout.addWidget(self.hello_label)
        self.layout.addWidget(self.new_game_button)
        self.layout.addWidget(self.continue_game_button)
        self.layout.setGeometry(QRect(196, 100, 220, 100))

    def newGameButtonClicked(self):
        self.main_window.new_game_flag = True
        self.main_window.display(3)

    def continueGameButtonClicked(self):
        self.main_window.new_game_flag = False
        self.main_window.display(2)
