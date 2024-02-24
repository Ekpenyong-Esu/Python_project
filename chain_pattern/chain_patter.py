"""
Chain of Responsibility pattern is a behavioral design pattern where a 
request is passed through a chain of handlers. Each handler decides either 
to process the request or to pass it along to the next handler in the chain.
"""

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, expense):
        if self.successor:
            self.successor.handle_request(expense)

class Manager(Handler):
    def handle_request(self, expense):
        if expense <= 100:
            print(f"Manager approves expense of ${expense}")
        elif self.successor:
            self.successor.handle_request(expense)

class Director(Handler):
    def handle_request(self, expense):
        if expense <= 500:
            print(f"Director approves expense of ${expense}")
        elif self.successor:
            self.successor.handle_request(expense)

class CEO(Handler):
    def handle_request(self, expense):
        if expense <= 1000:
            print(f"CEO approves expense of ${expense}")
        else:
            print(f"Expense of ${expense} is too high. Request denied.")

# Usage
manager = Manager()
director = Director(manager)
ceo = CEO(director)

# Client submits expense requests
ceo.handle_request(50)    # Manager approves expense of $50
ceo.handle_request(200)   # Director approves expense of $200
ceo.handle_request(800)   # CEO approves expense of $800
ceo.handle_request(1200)  # Expense of $1200 is too high. Request denied.
