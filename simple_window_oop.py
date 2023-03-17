import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Declare window class based on QWidget class
class window(QWidget):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)

        self.resize(200,50)
        self.setWindowTitle("PyQt5")
        self.label = QLabel(self)
        self.label.setText("Hello World")
        
        # change font
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50,20)

def main():
    # Create an application object of QApplication class
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    # Enter the mainloop of application by app.exec_() method
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()