"""
The Observer Pattern is a behavioral design pattern where an object, 
known as the subject, maintains a list of its dependents, known as observers, 
that are notified of any state changes, typically by calling one of their methods. 
This pattern is widely used to implement distributed event handling systems. 
Here's a simple example in Python to illustrate the Observer Pattern:
"""


# Observer interface
class Observer:
    def update(self, message):
        pass


# Concrete Observer 1
class ConcreteObserver1(Observer):
    def update(self, message):
        print(f"Observer 1 received: {message}")


# Concrete Observer 2
class ConcreteObserver2(Observer):
    def update(self, message):
        print(f"Observer 2 received: {message}")


# Subject
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


# Concrete Subject
class ConcreteSubject(Subject):
    def change_state(self, new_state):
        print(f"Subject state changed to: {new_state}")
        self.notify_observers(f"State changed to: {new_state}")


# Client code
observer1 = ConcreteObserver1()
observer2 = ConcreteObserver2()

subject = ConcreteSubject()
subject.add_observer(observer1)
subject.add_observer(observer2)

# Triggering a state change in the subject
subject.change_state("New State")
