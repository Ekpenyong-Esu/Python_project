
# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)

# Client Code
if __name__ == "__main__":
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()

    cart1 = ShoppingCart(credit_card_payment)
    cart1.checkout(100)

    cart2 = ShoppingCart(paypal_payment)
    cart2.checkout(50)
