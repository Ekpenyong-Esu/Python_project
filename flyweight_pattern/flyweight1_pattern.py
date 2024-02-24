from collections import defaultdict


class CoffeeFlavor:
    MOCHA = 'mocha'
    LATTE = 'latte'
    CAPPUCCINO = 'cappuccino'


class CoffeeOrder:
    def __init__(self, flavor):
        self.flavor = flavor

    def serve(self):
        print(f"Serving {self.flavor} coffee")


class CoffeeOrderFactory:
    def __init__(self):
        self.flavor_map = defaultdict(CoffeeOrder)

    def get_order(self, flavor):
        if flavor not in self.flavor_map:
            self.flavor_map[flavor] = CoffeeOrder(flavor)
        return self.flavor_map[flavor]


factory = CoffeeOrderFactory()

order1 = factory.get_order(CoffeeFlavor.MOCHA)
order1.serve()

order2 = factory.get_order(CoffeeFlavor.MOCHA)
order2.serve()

print(order1 is order2)  # True
