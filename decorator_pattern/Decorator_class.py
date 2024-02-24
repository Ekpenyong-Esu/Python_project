"""
The Decorator design pattern is a structural pattern that allows behavior 
to be added to individual objects, dynamically, without affecting the behavior 
of other objects from the same class. This pattern is often used in situations 
where subclassing would result in a proliferation of subclasses to handle all 
the combinations of features.
"""

from dataclasses import dataclass

# Base data class
@dataclass
class Component:
    name: str

    def operation(self) -> str:
        return f"{self.name}: Base operation"

# Decorator class
class Decorator(Component):
    def __init__(self, component: Component):
        self.component = component

    def operation(self) -> str:
        return f"{self.name}: Decorated operation"

# Concrete decorator
@dataclass
class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"{self.name}: ConcreteDecoratorA operation, {super().operation()}"

# Another concrete decorator
@dataclass
class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"{self.name}: ConcreteDecoratorB operation, {super().operation()}"

# Usage
if __name__ == "__main__":
    component = Component("Component")
    decorated_component_a = ConcreteDecoratorA(component)
    decorated_component_b = ConcreteDecoratorB(decorated_component_a)

    print(decorated_component_b.operation())
   