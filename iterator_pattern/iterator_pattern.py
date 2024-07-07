"""
The Iterator design pattern in Python is used to provide
a way to access the elements of an aggregate object sequentially 
without exposing its underlying representation. It also allows for 
iterating over collections in a uniform way.
"""

from abc import ABC, abstractmethod

class Iterator(ABC):
    """Interface for iterators."""

    @abstractmethod
    def has_next(self):
        """Returns True if there are more elements to iterate over."""
        raise NotImplementedError

    @abstractmethod
    def next(self):
        """Returns the next element in the iteration."""
        raise NotImplementedError


class ConcreteIterator(Iterator):
    """Concrete Iterator implementation."""

    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if not self.has_next():
            raise StopIteration("No more elements to iterate over")
        element = self._collection[self._index]
        self._index += 1
        return element


class Aggregate(ABC):
    """Interface for aggregates."""


    @abstractmethod
    def create_iterator(self):
        """Returns an iterator for the aggregate."""
        raise NotImplementedError


class ConcreteAggregate(Aggregate):
    """Concrete Aggregate implementation."""

    def __init__(self):
        self._collection = []

    def add_item(self, item):
        """Adds an item to the collection."""
        self._collection.append(item)

    def create_iterator(self):
        return ConcreteIterator(self._collection)


# Example usage:
if __name__ == "__main__":
    aggregate = ConcreteAggregate()
    aggregate.add_item("Item 1")
    aggregate.add_item("Item 2")
    aggregate.add_item("Item 3")

    iterator = aggregate.create_iterator()

    while iterator.has_next():
        print(iterator.next())


