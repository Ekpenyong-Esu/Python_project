from __future__ import annotations
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class ShapeDecorator(Shape):
    def __init__(self, decorated_shape: Shape) -> None:
        self.decorated_shape = decorated_shape

    def draw(self) -> None:
        self.decorated_shape.draw()


class RedShapeDecorator(ShapeDecorator):
    def draw(self) -> None:
        self.decorated_shape.draw()
        print("Coloring it red")
        
if __name__ == "__main__":
    circle = Circle()
    red_circle = RedShapeDecorator(Circle())

    print("Circle with normal color:")
    circle.draw()

    print("\nCircle colored red:")
    red_circle.draw()