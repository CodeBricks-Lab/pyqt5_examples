import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
def window():
    app = QApplication(sys.argv)

    win = QWidget()

    

    

    '''
    QFormLayout is a convenient way to create two column form, 
    where each row consists of an input field associated with a label. 
    As a convention, the left column contains the label and the right column contains an input field. 
    There are mainly three overloaded versions of addRow() method that are commonly used.
    '''
    fbox = QFormLayout()
    
    # name input
    l1 = QLabel("Name")
    nm = QLineEdit()
    fbox.addRow(l1,nm)

    # address input
    l2 = QLabel("Address")
    add1 = QLineEdit()
    add2 = QLineEdit()

    vbox = QVBoxLayout()
    vbox.addWidget(add1)
    vbox.addWidget(add2)

    fbox.addRow(l2,vbox)

    # sex input
    hbox = QHBoxLayout()
    r1 = QRadioButton("Male")
    r2 = QRadioButton("Female")
    hbox.addWidget(r1)
    hbox.addWidget(r2)
    hbox.addStretch()

    fbox.addRow(QLabel("sex"),hbox)

    # submit/cancel button
    fbox.addRow(QPushButton("Submit"),QPushButton("Cancel"))

    win.setLayout(fbox)
    win.setWindowTitle("PyQt5 Form Layout")
    win.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()