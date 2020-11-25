import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from ArchivosForm import Ui_ArchivosForm

class MainWindow(qtw.QWidget, Ui_ArchivosForm): #or qtw.QMainWindow
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        # code goes here

        self.show()

app = qtw.QApplication(sys.argv)
w= MainWindow()

sys.exit(app.exec_())
