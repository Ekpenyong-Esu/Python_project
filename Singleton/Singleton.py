from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class Singleton:
    _instance = None  # Class Attribute

    def __new__(cls, *args, **kwargs):  # The new is a special method that is called to create a new instance of the class
        if cls._instance is None:       # We override this method to control the creation of new instances of the class
                                        # The new method is a static method, so we don't need to use the @staticmethod decorator
            print("Creating Singleton instance")
            cls._instance = super().__new__(cls, *args, **kwargs)  # If the instance is None, we create a new instance of the class
        return cls._instance                                      # we call the superclass's __new__ method to create a new instance of the class

    def __init__(self): # This is a standard initializer method in Python. It's called after the instance has been created 
                        # and is used to initialize the instance variables.
        if hasattr(self, "initialized"): #If the instance hasn't been initialized yet, we set an attribute initialized on the instance to indicate 
            # that initialization has been done. This prevents the initialization process from being executed again if the constructor is called again
            return
        print("Creating Singleton instance")
        self.initialized = True
        # Initialize any instance variables here

class MainWindow(QMainWindow, Singleton):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Singleton Example")
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton("Click me", self)
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print("Button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
