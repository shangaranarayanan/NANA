# ==========================================
# PyQt Basics - Beginner Friendly Explanation
# ==========================================
# PyQt is used to create GUI (Graphical User Interface)
# applications in Python.
#
# Install PyQt5:
# pip install PyQt5
#
# This file explains:
# 1. QApplication
# 2. QWidget
# 3. QLabel
# 4. QPushButton
# 5. QLineEdit
# 6. Layouts
# 7. Signals and Slots
# ==========================================

# Import required modules
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QMessageBox
)


# Create a class for the main window
class MyWindow(QWidget):

    # Constructor
    def __init__(self):
        super().__init__()

        # -----------------------------
        # Window Settings
        # -----------------------------
        self.setWindowTitle("PyQt Beginner Demo")
        self.setGeometry(200, 200, 400, 250)

        # -----------------------------
        # Create Widgets
        # -----------------------------

        # QLabel -> Used to display text
        self.label = QLabel("Enter your name:")

        # QLineEdit -> Text input box
        self.textbox = QLineEdit()
        self.textbox.setPlaceholderText("Type here...")

        # QPushButton -> Button widget
        self.button = QPushButton("Submit")

        # -----------------------------
        # Signals and Slots
        # -----------------------------
        # When button is clicked,
        # call show_message function
        self.button.clicked.connect(self.show_message)

        # -----------------------------
        # Layout
        # -----------------------------
        # QVBoxLayout arranges widgets vertically
        layout = QVBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.button)

        # Set layout to window
        self.setLayout(layout)

    # ---------------------------------
    # Function for Button Click Event
    # ---------------------------------
    def show_message(self):

        # Get text from textbox
        name = self.textbox.text()

        # If textbox is empty
        if name == "":
            QMessageBox.warning(self, "Warning", "Please enter your name")

        # If textbox has value
        else:
            QMessageBox.information(
                self,
                "Welcome",
                f"Hello {name}! Welcome to PyQt"
            )


# ==========================================
# Main Program
# ==========================================

# QApplication manages the GUI application
app = QApplication(sys.argv)

# Create window object
window = MyWindow()

# Show the window
window.show()

# Execute application
sys.exit(app.exec_())


# ==========================================
# IMPORTANT PYQT CONCEPTS
# ==========================================
# QApplication
#     Main application object.
#     Required for every PyQt program.
#
# QWidget
#     Base class for windows and widgets.
#
# QLabel
#     Displays text.
#
# QPushButton
#     Creates a clickable button.
#
# QLineEdit
#     Used for text input.
#
# Layouts
#     Organize widgets automatically.
#     Example:
#       QVBoxLayout -> Vertical
#       QHBoxLayout -> Horizontal
#
# Signals and Slots
#     Used for event handling.
#     Example:
#       button.clicked.connect(function)
#
# QMessageBox
#     Used to show popup messages.
# ==========================================


# ==========================================
# HOW TO RUN
# ==========================================
# 1. Install PyQt5
#    pip install PyQt5
#
# 2. Save file as:
#    pyqt_demo.py
#
# 3. Run:
#    python pyqt_demo.py
# ==========================================
