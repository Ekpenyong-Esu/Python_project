"""
The visitor pattern allows adding new operations to existing 
object structures without modifying them. It separates the algorithm 
from the object structure it operates on.
"""

# Visitor interface
class Visitor:
    def visit_element_a(self, element_a):
        pass

    def visit_element_b(self, element_b):
        pass

# Concrete Visitor
class ConcreteVisitor(Visitor):
    def visit_element_a(self, element_a):
        print("Visiting ElementA")

    def visit_element_b(self, element_b):
        print("Visiting ElementB")

# Element interface
class Element:
    def accept(self, visitor):
        pass

# Concrete Elements
class ElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)

class ElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)

# Client Code
if __name__ == "__main__":
    element_a = ElementA()
    element_b = ElementB()

    visitor = ConcreteVisitor()

    element_a.accept(visitor)
    element_b.accept(visitor)
