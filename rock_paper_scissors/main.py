import sys
import random
from PySide6.QtWidgets import QApplication,QMainWindow
from ui_main_ui import Ui_MainWindow

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
game = Game()
game.show()
app.exec()