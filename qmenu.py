import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create a File menu and add it to the menu bar
        file_menu = self.menuBar().addMenu('File')

        # Create a New action and add it to the File menu
        new_action = QAction('New', self)
        file_menu.addAction(new_action)

        # Create a Save action and add it to the File menu
        save_action = QAction('Save', self)
        file_menu.addAction(save_action)

        # Create a Quit action and add it to the File menu
        quit_action = QAction('Quit', self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        # Create an Edit menu and add it to the menu bar
        edit_menu = self.menuBar().addMenu('Edit')

        # Create a Cut action and add it to the Edit menu
        cut_action = QAction('Cut', self)
        edit_menu.addAction(cut_action)

        # Create a Copy action and add it to the Edit menu
        copy_action = QAction('Copy', self)
        edit_menu.addAction(copy_action)

        # Create a Paste action and add it to the Edit menu
        paste_action = QAction('Paste', self)
        edit_menu.addAction(paste_action)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
