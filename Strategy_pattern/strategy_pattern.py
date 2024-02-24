
import math

class strategy:
    """
    The Strategy Pattern is a behavioral design pattern that defines a family of algorithms,
    encapsulates each algorithm, and makes them interchangeable. It allows a client to 
    choose an algorithm from a family of algorithms at runtime without altering the code
    that uses the algorithm. This pattern promotes the principle of favoring composition 
    over inheritance.  
    """
    def __init__(self, func=None):
        if func:
            self.execute = func

    def calculate(self):
        print("Calculating...")



class Addition(strategy):
    def calculate(self, a, b):
        print("Addition")
        return a + b
    
class Subtraction(strategy):
    def calculate(self, a, b):
        print("Subtraction")
        return a - b
    
class Multiplication(strategy):
    def calculate(self, a, b):
        print("Multiplication")
        return a * b
    
class Division(strategy):
    def calculate(self, a, b):
        print("Division")
        return a / b
    
class Modulus(strategy):
    def calculate(self, a, b):
        print("Modulus")
        return a % b
    
class Exponentiation(strategy):
    def calculate(self, a, b):
        print("Exponentiation")
        return a ** b
    
class Floor_Division(strategy):
    def calculate(self, a, b):
        print("Floor_Division")
        return a // b
    
class Square(strategy):
    def calculate(self, a):
        print("Square")
        return a * a
    
class Square_Root(strategy):
    def calculate(self, a):
        print("Square_Root")
        return a ** 0.5
    
class Cube(strategy):
    def calculate(self, a):
        print("Cube")
        return a * a * a
    
class Cube_Root(strategy):
    def calculate(self, a):
        print("Cube_Root")
        return a ** (1/3)
    
class Inverse(strategy):    
    def calculate(self, a):
        print("Inverse")
        return 1 / a
    
class Factorial(strategy):        
    def calculate(self, a):
        print("Factorial")
        return math.factorial(a)
    

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute(self, a, b):
        return self._strategy.calculate(a, b)
    
    def execute_1(self, a):
        return self._strategy.calculate(a)
    
    def set_strategy(self, strategy):
        self._strategy = strategy


if __name__ == "__main__":

    strategy = Addition()
    context = Context(strategy)
    print(context.execute(10, 5))
    print(" ")

    strategy = Subtraction()
    context.set_strategy(strategy)
    print(context.execute(10, 5))
    print(" ")

    strategy = Multiplication()
    context.set_strategy(strategy)
    print(context.execute(10, 5))
    print(" ")

    strategy = Division()
    context.set_strategy(strategy)
    print(context.execute(10, 5))
    print(" ")

    strategy = Modulus()
    context.set_strategy(strategy)
    print(context.execute(10, 5), "\n") 

    strategy = Exponentiation()
    context.set_strategy(strategy)  
    print(context.execute(10, 5), "\n")

    strategy = Floor_Division()
    context.set_strategy(strategy)
    print(context.execute(10, 5), "\n")   

    strategy = Square()
    context.set_strategy(strategy)
    print(context.execute_1(10), "\n")

    strategy = Square_Root()
    context.set_strategy(strategy)
    print(context.execute_1(10), "\n")

    strategy = Cube()
    context.set_strategy(strategy)
    print(context.execute_1(10), "\n")


    strategy = Cube_Root()
    context.set_strategy(strategy)
    print(context.execute_1(10), "\n")

    strategy = Inverse()
    context.set_strategy(strategy)
    print(context.execute_1(10), "\n")

    strategy = Factorial()
    context.set_strategy(strategy)
    print(context.execute_1(10), "\n")

    
