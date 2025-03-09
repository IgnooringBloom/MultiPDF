import sys # this provides access to command line and many more system utilities
from PyQt6.QtWidgets import QApplication # This imports the core QApplication class that manages the application's control flow and GUI settings
from ui.main_window import MainWindow # This class handles the main UI layout and widgets

def main():
    app = QApplication(sys.argv) # This creates an application instance and manages the GUI as well. 
                                 # passing sys.argv as argument to QApplication. Here the sys.argv contains all the command line arguments.
    window = MainWindow() # This initializes the main window widget. We are calling the mainwindow class.
    window.show() # this makes the window visible on the screen.
    sys.exit(app.exec()) # we exit sys when we quit the main app.exec file. If not then app.exec is initialized in an infinite loop.

if __name__ == "__main__":
    main()