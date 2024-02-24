"""
The Visitor Pattern is a behavioral design pattern that defines a 
mechanism for separating algorithms from the objects on which they operate. 
It allows you to define new operations without changing the classes of the elements on which it operates. 
The pattern is particularly useful when you have a set of classes with a stable structure, 
but you want to define and perform various operations on these classes.
"""

from abc import ABC, abstractmethod

# Element interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# ConcreteElement
class TextElement(Element):
    def accept(self, visitor):
        visitor.visit_text(self)

    def get_text(self):
        return "This is a text element."

class ImageElement(Element):
    def accept(self, visitor):
        visitor.visit_image(self)

    def get_image(self):
        return "This is an image element."

# Visitor interface
class Visitor(ABC):
    @abstractmethod
    def visit_text(self, text_element):
        pass

    @abstractmethod
    def visit_image(self, image_element):
        pass

# ConcreteVisitor
class HighlightVisitor(Visitor):
    def visit_text(self, text_element):
        print(f"Highlighting text: {text_element.get_text()}")

    def visit_image(self, image_element):
        print(f"Cannot highlight images: {image_element.get_image()}")

# ConcreteVisitor
class CountVisitor(Visitor):
    text_count = 0
    image_count = 0

    def visit_text(self, text_element):
        self.text_count += 1

    def visit_image(self, image_element):
        self.image_count += 1

# ObjectStructure
class Document:
    def __init__(self, elements):
        self.elements = elements

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)

# Usage
text_element = TextElement()
image_element = ImageElement()

document = Document([text_element, image_element])

highlight_visitor = HighlightVisitor()
count_visitor = CountVisitor()

document.accept(highlight_visitor)
document.accept(count_visitor)

print(f"Text count: {count_visitor.text_count}")
print(f"Image count: {count_visitor.image_count}")
