"""
The Adapter Pattern is a structural design pattern that allows the interface 
of an existing class to be used as another interface. It is often used to make existing 
classes work with others without modifying their source code. Here's a simple explanation and an example 
in a hypothetical programming language:
"""

# Existing class with specific interface
class Adaptee:
    def specific_request(self):
        return "Specific request"


# The default Target interface
class Target:
    def request(self):
        pass


# Adapter
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()


# Client code
def client_code(target):
    result = target.request()
    print(result)


# Using Adaptee directly (before using the adapter)
adaptee_instance = Adaptee()
print("Adaptee directly:", adaptee_instance.specific_request())

# Using Adapter to make Adaptee work as Target
adapter_instance = Adapter(adaptee_instance)
print("Using Adapter:", end=" ")
client_code(adapter_instance)
