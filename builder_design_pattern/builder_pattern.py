"""
The Builder Design Pattern is a creational pattern that allows for the construction of 
a complex object step by step. It separates the construction of a complex object 
from its representation, so that the same construction process can create different 
representations.
"""


# Product
class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def display(self):
        print("Product parts:", ", ".join(self.parts))


# Builder interface
class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_result(self):
        pass


# Concrete Builder A
class ConcreteBuilderA(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("Part A1")

    def build_part_b(self):
        self.product.add_part("Part B1")

    def get_result(self):
        return self.product


# Concrete Builder B
class ConcreteBuilderB(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("Part A2")

    def build_part_b(self):
        self.product.add_part("Part B2")

    def get_result(self):
        return self.product


# Director
class Director:
    def construct(self, builder):
        builder.build_part_a()
        builder.build_part_b()


# Client code
if __name__ == "__main__":
    director = Director()

    builder_a = ConcreteBuilderA()
    director.construct(builder_a)
    product_a = builder_a.get_result()
    product_a.display()

    builder_b = ConcreteBuilderB()
    director.construct(builder_b)
    product_b = builder_b.get_result()
    product_b.display()
