import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

"""
This widget is a file selector dialog. 
It enables the user to navigate through the file system and select a file to open or save. 
The dialog is invoked either through static functions or by calling exec_() function on the dialog object.
Static functions of QFileDialog class (getOpenFileName() and getSaveFileName()) call the native file dialog of the current operating system.
A file filter can also applied to display only files of the specified extensions. 
The starting directory and default file name can also be set.

Important methods and enumerations of QFileDialog class are listed below:

getOpenFileName(): Returns name of the file selected by the user to open it
getSaveFileName(): Uses the file name selected by the user to save the file
setacceptMode(): Determines whether the file box acts as open or save dialog
QFileDialog.AcceptOpen
QFileDialog.AcceptSave

setFileMode(): Type of selectable files. Enumerated constants are 
- QFileDialog.AnyFile
- QFileDialog.ExistingFile
- QFileDialog.Directory 
- QFileDialog.ExistingFiles

setFilter(): Displays only those files having mentioned extension
"""
class filedialogdemo(QWidget):
    def __init__(self, parent = None):
        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.btn = QPushButton("QFileDialog static method demo") 
        self.btn.clicked.connect(self.getfile)
        layout.addWidget(self.btn)
        self.le = QLabel("")
        layout.addWidget(self.le)
        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")
       
    def getfile(self):
        # for windows 
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'd:\\',"Image files (*.jpg *.png)")
        # for others
        # fname = QFileDialog.getOpenFileName(self, 'Open file', '/Users/',"Image files (*.jpg *.png)")
        self.le.setPixmap(QPixmap(fname[0]))
 
def main():
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
