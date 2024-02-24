# Component Interface
class Engine:
    """
    Certainly! The Composition Design Pattern is a structural design pattern where objects
    are combined to form more complex structures. It emphasizes building a system by
    composing objects instead of relying on inheritance. Here's a simple example in
    Python to illustrate the Composition Design Pattern:
    """
    def start(self):
        pass

# Concrete Component
class ElectricEngine(Engine):
    def start(self):
        return "Electric engine started"

# Another Concrete Component
class GasolineEngine(Engine):
    def start(self):
        return "Gasoline engine started"

# Composite
class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return f"Car with {self.engine.start()}"

# Client Code
if __name__ == "__main__":
    electric_engine = ElectricEngine()
    gasoline_engine = GasolineEngine()

    electric_car = Car(electric_engine)
    gasoline_car = Car(gasoline_engine)

    print(electric_car.start())  # Output: Car with Electric engine started
    print(gasoline_car.start())  # Output: Car with Gasoline engine started
