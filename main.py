import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow_ui import Ui_ui_mainwindow
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ui_mainwindow()
        self.ui.setupUi(self)
        self.araye = [] 

        self.buttons = [
            [self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
            [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btbn_8],
            [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
            [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16],
        ]

        for i in range(4):
            for j in range(4):
                r = random.randint(1, 16)
                while r in self.araye:
                    r = random.randint(1, 16)
                else:                
                    self.buttons[i][j].setText(str(r))
                    self.buttons[i][j].clicked.connect(partial(self.play,i,j))
                    self.araye.append(r)
                if r== 16:
                    self.empty_i = i
                    self.empty_j = j
                    self.buttons[i][j].hide()

    def play(self,i,j):
        if (i == self.empty_i and (j== self.empty_j -1 or j == self.empty_j +1)) or (j== self.empty_j and (i== self.empty_i -1 or i== self.empty_i + 1)):
            ...
            

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()
