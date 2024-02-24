from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts 
    of the Product objects.
    """
    
    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None: 
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    Concrete Builder1 implements the Builder interface.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Concrete Builder1 builds and assembles Product1.
        """
        return self._product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1():
    """
    Product 1 represents a complex object that is built.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is responsible for managing the correct sequence of object
    creation steps. The client uses the Director rather than interacting 
    with the builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code 
        passes to it. This way, the client code can alter the final type of 
        the newly assembled product.
        """
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director, and 
    then initiates the construction process. The end result is retrieved from 
    the builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product:")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product:")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")