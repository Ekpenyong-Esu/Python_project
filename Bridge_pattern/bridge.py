"""
The Bridge Pattern is a structural design pattern that separates abstraction 
from implementation so that the two can vary independently. It involves creating a 
bridge interface, which contains a reference to the implementation interface. 
This helps in decoupling abstraction and implementation, allowing them to evolve independently.
"""

# Abstraction
class Shape:
    def __init__(self, implementation):
        self.implementation = implementation

    def draw(self):
        pass


# Implementor
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass


# Concrete Implementor 1
class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API 1 Drawing a circle at ({x}, {y}) with radius {radius}")


# Concrete Implementor 2
class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API 2 Drawing a circle at ({x}, {y}) with radius {radius}")


# Refined Abstraction
class Circle(Shape):
    def __init__(self, x, y, radius, implementation):
        super().__init__(implementation)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.implementation.draw_circle(self.x, self.y, self.radius)


# Client code
api_implementation_1 = DrawingAPI1()
api_implementation_2 = DrawingAPI2()

circle_1 = Circle(1, 2, 3, api_implementation_1)
circle_2 = Circle(5, 7, 11, api_implementation_2)

circle_1.draw()
circle_2.draw()
