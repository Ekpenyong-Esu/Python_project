import os

# Component Interface
class FileSystemComponent:
    """
    To recursively print the files in a directory using composition in Python, you can create
    a composite class that represents both files and directories. Here's an example using 
    composition 
    """
    def display(self):
        pass

# Leaf: Concrete Component for File
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"File: {self.name}")

# Composite: Concrete Component for Directory
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()

# Client Code to recursively print directory structure
def print_directory_structure(component, indent=""):
    component.display()
    if isinstance(component, Directory):
        for child in component.children:
            print_directory_structure(child, indent + "  ")

# Example Usage
if __name__ == "__main__":
    # Creating a sample directory structure
    root = Directory("Root")
    documents = Directory("Documents")
    pictures = Directory("Pictures")
    file1 = File("document1.txt")
    file2 = File("picture1.jpg")

    root.add(documents)
    root.add(pictures)
    documents.add(file1)
    pictures.add(file2)

    # Recursively print directory structure
    print_directory_structure(root)
