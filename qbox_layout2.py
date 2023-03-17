import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)

    win = QWidget()

    b1 = QPushButton("Button1")
    b2 = QPushButton("Button2")

    hbox = QHBoxLayout()
    hbox.addWidget(b1)
    hbox.addStretch()
    hbox.addWidget(b2)

    win.setLayout(hbox)
    win.setWindowTitle("PyQt")
    win.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
