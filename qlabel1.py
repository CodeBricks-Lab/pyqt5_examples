import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    l1 = QLabel()
    l2 = QLabel()
    l3 = QLabel()
    l4 = QLabel()
    l1.setText("Hello World")
    l4.setText('<a href="https://www.example.com">Click Me!</a>') 
    l2.setText("welcome to Python GUI Programming")

    l1.setAlignment(Qt.AlignCenter)
    l3.setAlignment(Qt.AlignCenter)
    l4.setAlignment(Qt.AlignRight)

    l3.setPixmap(QPixmap("python.jpg"))

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()
    vbox.addWidget(l4)

    l4.setOpenExternalLinks(True)

    win.setLayout(vbox)
    win.setWindowTitle("QLabel Demo")
    win.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
