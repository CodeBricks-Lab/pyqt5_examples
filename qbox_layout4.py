import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Button Layout")
        self.setGeometry(300, 300, 300, 200)

        # Create buttons
        button1 = QPushButton("Button 1", self)
        button2 = QPushButton("Button 2", self)
        button3 = QPushButton("Button 3", self)
        button4 = QPushButton("Button 4", self)
        button5 = QPushButton("Button 5", self)
        button6 = QPushButton("Button 6", self)

        # Create layouts
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        vbox = QVBoxLayout()

        # Add buttons to layouts
        hbox1.addWidget(button1)
        hbox1.addWidget(button2)

        hbox2.addWidget(button3)
        hbox2.addWidget(button4)

        hbox3.addWidget(button5)
        hbox3.addWidget(button6)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
