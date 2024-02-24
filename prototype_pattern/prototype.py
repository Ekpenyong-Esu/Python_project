"""
The Prototype Pattern is a creational design pattern that allows 
you to create new objects by copying an existing object, known as the prototype. 
This pattern involves creating new objects by copying an existing object, 
known as the prototype.
"""

import copy

# Prototype interface
class Prototype:
    def clone(self):
        pass


# Concrete Prototype
class ConcretePrototype(Prototype):
    def __init__(self, name):
        self.name = name

    def clone(self):
        return copy.deepcopy(self)


# Client code
prototype_instance = ConcretePrototype("Original Object")
print("Original Object Name:", prototype_instance.name)

# Creating a new object by cloning the prototype
clone_instance = prototype_instance.clone()
print("Cloned Object Name:", clone_instance.name)

# Modifying the cloned object does not affect the original
clone_instance.name = "Modified Object"
print("Original Object Name after Modification:", prototype_instance.name)
print("Cloned Object Name after Modification:", clone_instance.name)
