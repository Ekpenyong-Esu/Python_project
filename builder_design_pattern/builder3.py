# Product class with multiple attributes
class Product:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price

    def __str__(self):
        return f"Product{{name='{self.name}', type='{self.type}', price={self.price}}}"

# Builder interface
class ProductBuilder:
    def set_name(self, name):
        pass

    def set_type(self, type):
        pass

    def set_price(self, price):
        pass

    def build(self):
        pass

# Concrete implementation of the builder interface
class ConcreteProductBuilder(ProductBuilder):
    def __init__(self):
        self.product = Product("DefaultName", "DefaultType", 0)

    def set_name(self, name):
        self.product.name = name
        return self

    def set_type(self, type):
        self.product.type = type
        return self

    def set_price(self, price):
        self.product.price = price
        return self

    def build(self):
        return self.product

# Client code
def main():
    builder = ConcreteProductBuilder()

    # Constructing the product using the builder
    product = builder \
        .set_name("ExampleProduct") \
        .set_type("ExampleType") \
        .set_price(100) \
        .build()

    # Displaying the constructed product
    print(product)

if __name__ == "__main__":
    main()
