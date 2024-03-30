"""
The State pattern is a behavioral design pattern that allows an object 
to alter its behavior when its internal state changes. The pattern represents 
different states of an object as separate classes and delegates the state-specific behavior 
to these classes. The object, known as the context, maintains a reference to the current state 
object and switches between states as needed.
"""

from abc import ABC, abstractmethod

# State interface
class State:

    @abstractmethod
    def handle(self):
        pass

# Concrete States
class ConcreteStateA(State):
    def handle(self):
        print("Handling state A")

class ConcreteStateB(State):
    def handle(self):
        print("Handling state B")

# Context
class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle()

# Client Code
if __name__ == "__main__":
    # Create instances of concrete states
    state_a = ConcreteStateA()
    state_b = ConcreteStateB()

    # Create context with an initial state
    context = Context(state_a)

    # Request with the initial state
    context.request()

    # Change state and request again
    context.set_state(state_b)
    context.request()
