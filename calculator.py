import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        
        # Set window properties
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 300)
        
        # Set up the grid layout
        grid = QGridLayout()
        self.setLayout(grid)
        
        # Create the display widget
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        grid.addWidget(self.display, 0, 0, 1, 4)
        
        # Create the number buttons
        for i in range(10):
            button = QPushButton(str(i))
            button.clicked.connect(lambda x, n=i: self.add_to_display(n))
            row = (9 - i) // 3 + 1
            col = (i - 1) % 3
            grid.addWidget(button, row, col)
            
        # Create the operator buttons
        ops = ['+', '-', '*', '/', 'C', '=']
        for i, op in enumerate(ops):
            button = QPushButton(op)
            button.clicked.connect(lambda x, op=op: self.handle_operator(op))
            grid.addWidget(button, i // 2 + 1, i % 2 + 3)
        
        # Show the window
        self.show()
    
    def add_to_display(self, n):
        self.display.setText(self.display.text() + str(n))
    
    def handle_operator(self, op):
        if op == 'C':
            self.display.setText('')
        elif op == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText('Error')
        else:
            self.display.setText(self.display.text() + ' ' + op + ' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())