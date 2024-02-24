"""
The state design pattern involves defining a state interface and concrete state 
classes that implement the state interface. The state interface defines the behavior 
that changes with the object's state. The concrete state classes provide specific 
implementations of the behavior for each state.
"""

class VendingMachine:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price  # Add the product_price attribute
        self.state = NoMoneyState()

    def insert_money(self, amount):
        self.state.insert_money(self, amount)

    def dispense_product(self):
        self.state.dispense_product(self)

    def set_state(self, new_state):
        self.state = new_state

class NoMoneyState:
    def insert_money(self, vending_machine, amount):
        if amount >= vending_machine.product_price:  # this is retrieved directly from the vending_machine object
            vending_machine.set_state(HasMoneyState())
        else:
            print("Insufficient money. Please insert at least", vending_machine.product_price)

    def dispense_product(self, vending_machine):
        print("Please insert money first")

class HasMoneyState:
    def insert_money(self, vending_machine, amount):
        print("You can't insert more money when you already have enough")

    def dispense_product(self, vending_machine):
        print("Dispensing", vending_machine.product_name)
        vending_machine.set_state(NoMoneyState())

class OutOfStockState:
    def insert_money(self, vending_machine, amount):
        print("Product out of stock. Please try later")

    def dispense_product(self, vending_machine):
        print("Product out of stock. Please try later")

if __name__ == "__main__":
    vending_machine = VendingMachine("Coke", 25)  # Provide the product price
    vending_machine.insert_money(68)
    vending_machine.dispense_product()
