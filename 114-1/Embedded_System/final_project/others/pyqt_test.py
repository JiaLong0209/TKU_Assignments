
import serial


import sys
# Import QApplication and QWidget classes from PyQt5 to create a GUI application
from PyQt5.QtWidgets import QApplication, QWidget
# Create an instance of QApplication
# sys.argv is passed to handle command-line arguments for the application
app = QApplication(sys.argv)
# Create an instance of QWidget, serve as the main window for the application
window = QWidget()
# Set the title of the window to 'Example App'
window.setWindowTitle("Basic UI")
# Show the window on the screen
window.show()
# Start the application’s event loop
# sys.exit() ensures that the application exits cleanly when the window is closed
sys.exit(app.exec_())



