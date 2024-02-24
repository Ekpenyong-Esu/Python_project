from dataclasses import dataclass

# Base interface for the component
class Component:
    def operation(self) -> str:
        pass

# Concrete component
class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

# Base decorator
@dataclass
class Decorator(Component):
    component: Component

    def operation(self) -> str:
        return self.component.operation()

# Concrete decorator
@dataclass
class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"

# Another concrete decorator
@dataclass
class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


if __name__ == "__main__":
    # Creating a concrete component
    simple = ConcreteComponent()
    print("Result: ", simple.operation())

    # Decorating the component with ConcreteDecoratorA
    decorator1 = ConcreteDecoratorA(simple)
    print("Result: ", decorator1.operation())

    # Decorating the component with ConcreteDecoratorB
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Result: ", decorator2.operation())
