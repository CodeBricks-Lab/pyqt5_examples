import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    # Create an application object of QApplication class
    app = QApplication(sys.argv)
    
    # A QWidget object creates top level window. Add QLabel object in it
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(500,500,200,50)
    b.move(50,20)
    w.setWindowTitle("PyQt5")
    w.show()

    # Enter the mainloop of application by app.exec_() method.
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()