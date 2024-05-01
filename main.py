from PyQt6.QtWidgets import QApplication, QMainWindow
from simple_window import Ui_MainWindow  # Adjust this import based on your actual file location

def close_application():
    """Function to handle the button click event to close the application."""
    QApplication.instance().quit()

def main():
    import sys
    app = QApplication(sys.argv)
    
    # Set up the main window
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Connect the button click to the custom close_application function
    ui.pushButton.clicked.connect(close_application)

    # Connect the actionQuit action triggered signal to the same function
    ui.actionquit.triggered.connect(close_application)
    
    # Show the main window
    MainWindow.show()
    
    # Start the application's event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
