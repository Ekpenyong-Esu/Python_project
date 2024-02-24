"""
The Decorator Pattern is a structural design pattern that allows behavior 
to be added to an individual object, either statically or dynamically, without 
affecting the behavior of other objects from the same class. It's a way to extend 
the functionality of classes in a flexible and reusable manner.
"""


# Component interface
class Coffee:
    def cost(self):
        pass


# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5


# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()


# Concrete Decorator 1
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def __str__(self):
        return "Milk"


# Concrete Decorator 2
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def __str__(self):
        return "Sugar"


# Client code
simple_coffee = SimpleCoffee()
print("Cost of Simple Coffee:", simple_coffee.cost())

milk_coffee = MilkDecorator(simple_coffee)
print("Cost of Milk Coffee:", milk_coffee.cost())

sugar_milk_coffee = SugarDecorator(milk_coffee)
print("Cost of Sugar Milk Coffee:", sugar_milk_coffee.cost())

# You can also print the description of the coffee with decorators
print("Ingredients:", sugar_milk_coffee.__str__())
