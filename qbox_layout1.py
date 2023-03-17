import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)

    win = QWidget()

    b1 = QPushButton("Button1")
    b2 = QPushButton("Button2")
    '''
    QBoxLayout class lines up the widgets vertically or horizontally. 
    Its derived classes are QVBoxLayout (for arranging widgets vertically) and QHBoxLayout (for arranging widgets horizontally). 
    '''
    vbox = QVBoxLayout()
    vbox.addWidget(b1)
    
    # Creates empty stretchable box
    vbox.addStretch()
    vbox.addWidget(b2)

    win.setLayout(vbox)
    win.setWindowTitle("PyQt")
    win.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()