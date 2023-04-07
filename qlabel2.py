import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.label.setText('<a href="https://www.example.com">Click Me!</a>')
        self.label.setOpenExternalLinks(True)
        self.label.linkActivated.connect(self.handle_link_clicked)

    def handle_link_clicked(self, url):
        QDesktopServices.openUrl(QUrl(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
