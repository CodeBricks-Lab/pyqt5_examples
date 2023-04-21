from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton

"""
In this example, we define a WorkerThread class that performs a task and emits a progressChanged signal to update the progress bar. 
We also define a MainWindow class that creates a progress bar and a button to start the task. 
When the button is clicked, we disable the button and start the worker thread. 
The updateProgressBar slot is called when the progressChanged signal is emitted, and it updates the value of the progress bar. 
When the progress reaches 100%, we re-enable the button. 
Finally, we create an instance of the MainWindow class and start the application event loop.
"""
class WorkerThread(QThread):
    progressChanged = pyqtSignal(int)

    def run(self):
        for i in range(101):
            self.progressChanged.emit(i)
            self.msleep(50)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a progress bar
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(50, 50, 200, 25)
        self.progressBar.setValue(0)

        # Create a button to start the task
        self.startButton = QPushButton("Start", self)
        self.startButton.setGeometry(50, 100, 100, 25)
        self.startButton.clicked.connect(self.startTask)

        self.workerThread = WorkerThread()
        self.workerThread.progressChanged.connect(self.updateProgressBar)

    def startTask(self):
        self.startButton.setEnabled(False)
        self.workerThread.start()

    def updateProgressBar(self, progress):
        self.progressBar.setValue(progress)
        if progress == 100:
            self.startButton.setEnabled(True)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
