
"""
The Facade Pattern is a structural design pattern that provides a unified interface
to a set of interfaces in a subsystem. It defines a higher-level interface that makes 
the subsystem easier to use. This pattern involves a single class, known as the facade, 
which provides a simple, unified interface to a set of interfaces in a subsystem, making 
it easier to use and reducing dependencies.
"""


# Subsystem 1
class Subsystem1:
    def operation1(self):
        return "Subsystem 1, Operation 1"

    def operation2(self):
        return "Subsystem 1, Operation 2"


# Subsystem 2
class Subsystem2:
    def operation1(self):
        return "Subsystem 2, Operation 1"

    def operation2(self):
        return "Subsystem 2, Operation 2"


# Facade
class Facade:
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()

    def operation(self):
        result = []
        result.append(self.subsystem1.operation1())
        result.append(self.subsystem1.operation2())
        result.append(self.subsystem2.operation1())
        result.append(self.subsystem2.operation2())
        return result


# Client code
def client_code(facade):
    result = facade.operation()
    for operation_result in result:
        print(operation_result)


# Using the Facade to simplify the subsystems
facade_instance = Facade()
print("Using Facade:")
client_code(facade_instance)
