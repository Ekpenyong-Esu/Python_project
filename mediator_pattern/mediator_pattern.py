"""
The Mediator Pattern is a behavioral design pattern that defines 
an object (the mediator) that centralizes communication between a 
set of objects (colleagues). Instead of allowing direct connections 
between the objects, the mediator facilitates communication and coordination, 
promoting loose coupling between the components.
"""

from abc import ABC, abstractmethod

# Mediator interface
class AirTrafficControl(ABC):
    @abstractmethod
    def notify(self, sender, message):
        pass

# Concrete Mediator
class ATCMediator(AirTrafficControl):
    def __init__(self):
        self.airplanes = []

    def register_airplane(self, airplane):
        self.airplanes.append(airplane)

    def notify(self, sender, message):
        for airplane in self.airplanes:
            if airplane != sender:
                airplane.receive(message)

# Colleague interface
class Airplane(ABC):
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive(self, message):
        pass

# Concrete Colleague
class Airbus(Airplane):
    def send(self, message):
        print(f"Airbus {self.name} sends message: {message}")
        self.mediator.notify(self, message)

    def receive(self, message):
        print(f"Airbus {self.name} receives message: {message}")

class Boeing(Airplane):
    def send(self, message):
        print(f"Boeing {self.name} sends message: {message}")
        self.mediator.notify(self, message)

    def receive(self, message):
        print(f"Boeing {self.name} receives message: {message}")

# Usage
mediator = ATCMediator()

airbus1 = Airbus(mediator, "A380")
airbus2 = Airbus(mediator, "A320")
boeing1 = Boeing(mediator, "747")

mediator.register_airplane(airbus1)
mediator.register_airplane(airbus2)
mediator.register_airplane(boeing1)

airbus1.send("Cleared for landing.")  # the airplane is sending a message out to the mediator
boeing1.send("Roger that.")
