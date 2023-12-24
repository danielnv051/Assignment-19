import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from mainwindow import Ui_mainwindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()