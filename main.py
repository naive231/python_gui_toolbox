from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# Import the Ui_MainWindow class from your generated file
from simple_window import Ui_MainWindow

class CustomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create an instance of the Ui_MainWindow class
        self.ui = Ui_MainWindow()
        # Setup the user interface on this QMainWindow instance
        self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)  # Create an instance of QApplication
    window = CustomMainWindow()   # Create an instance of your QMainWindow subclass
    window.show()                 # Show the window
    sys.exit(app.exec())          # Start the application's event loop

if __name__ == "__main__":
    main()
