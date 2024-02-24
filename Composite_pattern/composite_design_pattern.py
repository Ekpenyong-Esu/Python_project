"""
The Composite design pattern is a structural pattern that 
lets you compose objects into tree structures to represent 
part-whole hierarchies. It allows clients to treat individual
objects and compositions of objects uniformly.
"""

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class Component:
    def operation(self):
        pass


class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        return f"File: {self.name}"


class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        result = f"Directory: {self.name}\n"
        for child in self.children:
            result += f"  {child.operation()}\n"
        return result


class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('File System Explorer')
        self.setGeometry(100, 100, 400, 300)

        # Create composite directory
        root = Composite("Root Directory")

        # Add individual files to the root directory
        root.add(Leaf("File 1.txt"))
        root.add(Leaf("File 2.doc"))

        # Create another composite directory
        subdirectory = Composite("Subdirectory")

        # Add files to the subdirectory
        subdirectory.add(Leaf("File 3.jpg"))
        subdirectory.add(Leaf("File 4.pdf"))

        # Add the subdirectory to the root directory
        root.add(subdirectory)

        # Display the composite structure
        label = QLabel(root.operation(), self)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(label)


if __name__ == '__main__':
    app = QApplication([])
    window = GUI()
    window.show()
    app.exec_()
