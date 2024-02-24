from abc import ABC, abstractmethod

# Product interface
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# Concrete Product A
class ConcreteProductA(Product):
    def operation(self):
        return "Product A operation"

# Concrete Product B
class ConcreteProductB(Product):
    def operation(self):
        return "Product B operation"

# Factory interface
class Factory(ABC):
    @abstractmethod
    def create_product(self, config: dict) -> Product:
        pass

# Concrete Factory A
class ConcreteFactoryA(Factory):
    def create_product(self, config: dict) -> Product:
        # You can customize the creation based on the config
        if config.get("type") == "special":
            return SpecialConcreteProductA()
        else:
            return ConcreteProductA()

# Concrete Factory B
class ConcreteFactoryB(Factory):
    def create_product(self, config: dict) -> Product:
        # You can customize the creation based on the config
        if config.get("size") == "large":
            return LargeConcreteProductB()
        else:
            return ConcreteProductB()

# Special Concrete Product A
class SpecialConcreteProductA(Product):
    def operation(self):
        return "Special Product A operation"

# Large Concrete Product B
class LargeConcreteProductB(Product):
    def operation(self):
        return "Large Product B operation"

# Client code
def client_code(factory: Factory, config: dict) -> None:
    product = factory.create_product(config)
    print(f"Client: {product.operation()}")

# Example usage
if __name__ == "__main__":
    print("App: Launched with ConcreteFactoryA.")
    config_A = {"type": "special"}
    client_code(ConcreteFactoryA(), config_A)
    print("\n")

    print("App: Launched with ConcreteFactoryB.")
    config_B = {"size": "large"}
    client_code(ConcreteFactoryB(), config_B)
