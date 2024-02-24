from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys

# Abstract Factory Interface
class GUIFactory:
    """
    GUIFactory is the abstract factory interface defining 
    methods for creating buttons and labels.
    """
    def create_button(self):
        pass

    def create_label(self):
        pass

# Concrete Factory 1
class MacOSFactory(GUIFactory):
    """
    MacOSFactory and WindowsFactory are concrete factory classes implementing 
    the GUIFactory interface. Each factory is responsible for creating buttons and 
    labels specific to their respective operating systems.
    """
    def create_button(self):
        return MacOSButton()

    def create_label(self):
        return MacOSLabel()

# Concrete Factory 2
class WindowsFactory(GUIFactory):
    """
    MacOSFactory and WindowsFactory are concrete factory classes implementing 
    the GUIFactory interface. Each factory is responsible for creating buttons and 
    labels specific to their respective operating systems.
    """
    def create_button(self):
        return WindowsButton()

    def create_label(self):
        return WindowsLabel()

# Abstract Product Interface
class Button:
    def paint(self):
        pass

# Concrete Product 1
class MacOSButton(Button):
    def paint(self):
        print("Rendering MacOS style button")

# Concrete Product 2
class WindowsButton(Button):
    def paint(self):
        print("Rendering Windows style button")

# Abstract Product Interface
class Label:
    def display(self):
        pass

# Concrete Product 1
class MacOSLabel(Label):
    def display(self):
        print("Displaying MacOS style label")

# Concrete Product 2
class WindowsLabel(Label):
    def display(self):
        print("Displaying Windows style label")

# Client
class Application:
    def __init__(self, factory):
        self.factory = factory

    def create_ui(self):
        button = self.factory.create_button()
        label = self.factory.create_label()

        button.paint()
        label.display()

if __name__ == "__main__":
    app = QApplication([])

    # Create a MacOS style UI
    macos_factory = MacOSFactory()
    macos_app = Application(macos_factory)
    macos_app.create_ui()

    # Create a Windows style UI
    windows_factory = WindowsFactory()
    windows_app = Application(windows_factory)
    windows_app.create_ui()

    sys.exit(app.exec_())
