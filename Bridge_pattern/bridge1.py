# Abstraction 
class Shape:
    def __init__(self, impl):
        self.impl = impl

    def draw(self):
        self.impl.draw()


# Implementor 
class DrawingAPI:
    def draw(self):
        pass
    

# Concrete ImplementorA 
class DrawingAPI1(DrawingAPI):
    def draw_circle(self, radius):
        print(f"API1 drawing circle of radius {radius}")


# Concrete ImplementorB
class DrawingAPI2(DrawingAPI):
    def draw_circle(self, radius):
        print(f"API2 drawing circle of radius {radius}")



# Refined Abstraction
class Circle(Shape):
    def __init__(self, impl, radius):
        super().__init__(impl)
        self.radius = radius

    def draw(self):
        self.impl.draw_circle(self.radius)



# Client 
shape = Circle(DrawingAPI1(), 5)
shape.draw()

shape = Circle(DrawingAPI2(), 7)
shape.draw()