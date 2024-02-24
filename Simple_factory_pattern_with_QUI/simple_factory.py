"""
simple_factory.py

Implements a simple factory pattern for creating Namer objects to parse names.
"""

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)


class BlueLabel(QLabel):
    """Derived class makes all labels blue."""

    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("color: blue")


class Namer:
    """Base Namer class."""

    def __init__(self):
        self.last = ""
        self.first = ""


class FirstFirst(Namer):
    """Derived namer class for First <space> Last."""

    def __init__(self, name_string):
        super().__init__()
        names = name_string.split(" ", 1)  # Split at the first space
        if len(names) > 1:
            self.first, self.last = names
        else:
            self.last = name_string


class LastFirst(Namer):
    """Derived Namer class for Last <comma> First."""

    def __init__(self, name_string):
        super().__init__()
        names = name_string.split(",", 1)  # Split at the first comma
        if len(names) > 1:
            self.last, self.first = names
        else:
            self.last = name_string


class NamerFactory:
    """
    he NameFactory returns an instance of
    the Namer class based on a comma.
    """

    def __init__(self, name_string):
        self.name = name_string

    def get_namer(self):
        """
        Decides based on a comma whether the last name
        is first and generates the correct Namer class.
        """

        if "," in self.name:
            return LastFirst(self.name)
        else:
            return FirstFirst(self.name)


class Builder(QWidget):
    """Builder class to create and manage the UI."""

    def __init__(self):
        super().__init__()
        self.build_ui()

    def clear_panel(self):
        """Clears all fields."""
        self.first_name_edit.clear()
        self.last_name_edit.clear()
        self.entry.clear()

    def compute(self):
        """Fills the fields using the namer from the Namer factory."""
        name = self.entry.text()
        namer_factory = NamerFactory(name)
        namer = namer_factory.get_namer()
        self.first_name_edit.setText(namer.first)
        self.last_name_edit.setText(namer.last)

    def build_ui(self):
        """Builds the UI."""
        self.setWindowTitle("Simple Factory")

        layout = QVBoxLayout(self)

        layout.addWidget(BlueLabel("Enter name"))

        self.entry = QLineEdit(self)
        layout.addWidget(self.entry)

        layout.addWidget(BlueLabel("First name:"))
        self.first_name_edit = QLineEdit(self)
        layout.addWidget(self.first_name_edit)

        layout.addWidget(BlueLabel("Last name:"))
        self.last_name_edit = QLineEdit(self)
        layout.addWidget(self.last_name_edit)

        self.bt_compute = QPushButton("Compute", self)
        self.bt_compute.clicked.connect(self.compute)
        layout.addWidget(self.bt_compute)

        self.bt_clear = QPushButton("Clear", self)
        self.bt_clear.clicked.connect(self.clear_panel)
        layout.addWidget(self.bt_clear)

        self.bt_quit = QPushButton("Quit", self)
        self.bt_quit.clicked.connect(self.close)
        layout.addWidget(self.bt_quit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    builder = Builder()
    builder.show()
    sys.exit(app.exec_())
