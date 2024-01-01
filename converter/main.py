import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QMessageBox
from ui_main import Ui_mainWindow

class Converter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.cal.clicked.connect(self.getItem)
        self.ui.combo_units.changeEvent()
        
    def getItem(self):
        txt = str(self.ui.combo_units.currentText())
        if txt == 'وزن':
            a = QMessageBox(text=txt)
            a.exec()



app = QApplication(sys.argv)
converter = Converter()
converter.show()
app.exec()

