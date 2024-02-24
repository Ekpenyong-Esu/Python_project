import copy


class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __repr__(self):
        return f"Shape(name='{self.name}', color='{self.color}')"

    def clone(self):
        # Deep copy to create a separate object
        return copy.deepcopy(self)

class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, name, color, width, height):
        super().__init__(name, color)
        self.width = width
        self.height = height

# Client code that uses the prototype pattern
        
if __name__ == "__main__":
    circle = Circle('Circle', 'Green', 5)
    rectangle = Rectangle('Rectangle', 'Red', 10, 20)

    new_circle = circle.clone()
    new_circle.color = 'Blue'
    new_circle.radius = 10

    print(circle)
    print(new_circle)

    new_rectangle = rectangle.clone()
    new_rectangle.color = 'Black'
    new_rectangle.width = 15

    print(rectangle)
    print(new_rectangle)