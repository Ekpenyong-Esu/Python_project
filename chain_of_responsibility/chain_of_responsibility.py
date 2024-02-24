"""
The Chain of Responsibility pattern is a behavioral design pattern that allows an o
bject to send a command without knowing which object will handle it. 
The request is passed along a chain of handlers until one of them handles the request.
"""

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == 'handler1':
            print("Handler 1 handling the request.")
        else:
            super().handle_request(request)

class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == 'handler2':
            print("Handler 2 handling the request.")
        else:
            super().handle_request(request)

class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if request == 'handler3':
            print("Handler 3 handling the request.")
        else:
            super().handle_request(request)

# Client code
if __name__ == "__main__":
    handler3 = ConcreteHandler3()
    handler2 = ConcreteHandler2(handler3)
    handler1 = ConcreteHandler1(handler2)

    # Send requests
    handler1.handle_request('handler1')
    handler1.handle_request('handler2')
    handler1.handle_request('handler3')
    handler1.handle_request('handler4')
