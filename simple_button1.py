import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QPushButton(w)
    b.setText("Hello World!")
    # A PushButton widget is added in the window and placed at a position 50 pixels towards right and 20 pixels below the top left position of the window.
    '''
    This Absolute Positioning, however, is not suitable because of the following reasons:
      - The position of the widget does not change even if the window is resized.
      - The appearance may not be uniform on different display devices with different resolutions.
      - Modification in the layout is difficult as it may need redesigning the entire form.
    '''
    b.move(50,20)
    
    # QWidget.setGeometry(xpos, ypos, width, height)
    w.setGeometry(100,100,300,100)
    w.setWindowTitle('PyQt5 Window')
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()