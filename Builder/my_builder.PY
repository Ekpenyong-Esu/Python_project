
"""
The Builder Design Pattern is a creational pattern that allows for the construction of 
a complex object step by step. It separates the construction of a complex object 
from its representation, so that the same construction process can create different 
representations.
"""


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QVBoxLayout, QWidget

# Builder Interface
class DocumentBuilder:
    def create_title(self):
        pass

    def create_body(self):
        pass

    def get_document(self):
        pass

# Concrete Builder
class TextDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.title = ""
        self.body = ""

    def create_title(self, title):
        self.title = title

    def create_body(self, body):
        self.body = body

    def get_document(self):
        return f"Title: {self.title}\n\n{self.body}"

# Director
class DocumentDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self, title, body):
        self.builder.create_title(title)
        self.builder.create_body(body)

# Client
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_document)
        self.file_menu.addAction(save_action)

    def save_document(self):
        title = input("Enter document title: ")
        body = self.text_edit.toPlainText()

        builder = TextDocumentBuilder()
        director = DocumentDirector(builder)
        director.construct(title, body)
        document = builder.get_document()

        with open(f"{title}.txt", "w") as file:
            file.write(document)
        print(f"Document '{title}' saved successfully.")

def main():
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
