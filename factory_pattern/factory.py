"""
The Factory Design Pattern is a creational design pattern that provides an interface 
for creating objects in a superclass, but allows subclasses to alter the type of objects 
that will be created. It is particularly useful when you have a class that cannot anticipate 
the class of objects it needs to create.
"""



from abc import ABC, abstractmethod

# Product interface
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# Concrete Product A
class ConcreteProductA(Product):
    def operation(self):
        return "Product A operation"

# Concrete Product B
class ConcreteProductB(Product):
    def operation(self):
        return "Product B operation"

# Creator interface
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: {product.operation()}"
        return result

# Concrete Creator A
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

# Concrete Creator B
class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# Client code
def client_code(creator: Creator) -> None:
    print(f"Client: {creator.some_operation()}", end="")

# Example usage
if __name__ == "__main__":
    print("App: Launched with ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    print("\n")

    print("App: Launched with ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
