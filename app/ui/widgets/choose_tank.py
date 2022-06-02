from typing import TYPE_CHECKING

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QBoxLayout, QLabel, QPushButton, QWidget

from app.constants import Default
from app.levels.tank_generator import (
    BigBulletTank,
    DefaultTank,
    FastBulletTank,
    HealthyTank,
)

if TYPE_CHECKING:
    from app.ui.main_window import MainWindow


class ChooseTankWidget(QWidget):
    def __init__(self, parent: "MainWindow"):
        super(ChooseTankWidget, self).__init__(parent)
        self.main_window = parent

        self.bg_label = QLabel(self)
        self.choose_label = QLabel(self)

        self.default_tank_button = QPushButton("Default tank", self)
        self.fast_bullet_tank_button = QPushButton("Fast bullet tank", self)
        self.healthy_tank_button = QPushButton("Healthy tank", self)
        self.big_bullet_tank_button = QPushButton("Big bullet tank", self)

        self.layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

    def init(self):
        self.bg_label.resize(612, 512)
        self.bg_label.setStyleSheet(
            f"background-image: url({Default.PATH_TO_MM_BACKGROUND});"
        )

        self.choose_label.setText(f"CHOOSE TANK, {self.main_window.username}!")
        self.choose_label.setFont(QFont("Verdana", 12, QFont.Bold))
        self.choose_label.setStyleSheet("QLabel { color : white; }")

        self.default_tank_button.clicked.connect(self.defaultTankButtonClicked)
        self.fast_bullet_tank_button.clicked.connect(self.fastBulletTankButtonClicked)
        self.healthy_tank_button.clicked.connect(self.healthyTankButtonClicked)
        self.big_bullet_tank_button.clicked.connect(self.bigBulletTankButtonClicked)

        self.layout.addWidget(self.choose_label)
        self.layout.addWidget(self.default_tank_button)
        self.layout.addWidget(self.fast_bullet_tank_button)
        self.layout.addWidget(self.healthy_tank_button)
        self.layout.addWidget(self.big_bullet_tank_button)
        self.layout.setGeometry(QRect(196, 100, 220, 100))

    def defaultTankButtonClicked(self):
        self.main_window.player_fabric = DefaultTank
        self.main_window.display(2)

    def fastBulletTankButtonClicked(self):
        self.main_window.player_fabric = FastBulletTank
        self.main_window.display(2)

    def bigBulletTankButtonClicked(self):
        self.main_window.player_fabric = BigBulletTank
        self.main_window.display(2)

    def healthyTankButtonClicked(self):
        self.main_window.player_fabric = HealthyTank
        self.main_window.display(2)
