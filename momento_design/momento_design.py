"""
The Memento design pattern is a behavioral design pattern that 
allows capturing and externalizing an object's internal state 
without violating encapsulation, so that the object can be 
restored to this state later.
"""


import copy

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        print("Originator: Setting state to", state)
        self._state = state

    def create_memento(self):
        print("Originator: Creating Memento")
        return Memento(copy.deepcopy(self._state))

    def restore_memento(self, memento):
        self._state = memento.get_state()
        print("Originator: Restoring state to", self._state)

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        print("Caretaker: Adding Memento")
        self._mementos.append(memento)

    def get_memento(self, index):
        print("Caretaker: Getting Memento")
        return self._mementos[index]


if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker()

    originator.set_state("State 1")
    caretaker.add_memento(originator.create_memento())

    originator.set_state("State 2")
    caretaker.add_memento(originator.create_memento())

    originator.set_state("State 3")
    caretaker.add_memento(originator.create_memento())

    print("Current state:", originator._state)

    originator.restore_memento(caretaker.get_memento(1))
    print("Restored to state:", originator._state)
