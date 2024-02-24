"""
The Interpreter pattern is a design pattern that defines a grammar 
for a language and provides an interpreter to interpret sentences 
in that language. It's useful when you need to interpret sentences 
or expressions in a specific domain language.
"""


from abc import ABC, abstractmethod

# Context
class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, variable, value):
        self.variables[variable] = value

    def get_variable(self, variable):
        return self.variables.get(variable)


# Abstract Expression
class Expression(ABC):

    @abstractmethod
    def interpret(self, context):
        pass


# Terminal Expression
class Variable(Expression):

    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        return context.get_variable(self.name)


# Non-terminal Expression
class Addition(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


# Client code
if __name__ == "__main__":
    context = Context()
    context.set_variable("x", 10)
    context.set_variable("y", 5)

    # Grammar: x + y
    expression = Addition(Variable("x"), Variable("y"))

    result = expression.interpret(context)
    print("Result:", result)  # Output: Result: 15
