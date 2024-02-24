from __future__ import annotations
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor: Handler = None) -> None:
        self._successor = successor

    def handle(self, request) -> None:
        handled = self._handle(request)

        if not handled and self._successor:
            self._successor.handle(request)

    @abstractmethod
    def _handle(self, request: str) -> bool:
        pass

class ConcreteHandler1(Handler):
    def _handle(self, request: str) -> bool:
        if request == 'request1':
            print('Handler1 handled request1')
            return True
        return False

class DefaultHandler(Handler):
    def _handle(self, request: str) -> bool:
        print('Default handler')
        return True

class Client:
    def __init__(self, handler: Handler) -> None:
        self._handler = handler

    def delegate(self, requests) -> None:
        for request in requests:
            self._handler.handle(request)

# Create handlers        
handler1 = ConcreteHandler1()
default = DefaultHandler()
handler1.successor = default

# Client
requests = ["request1", "request2"]
client = Client(handler1)
client.delegate(requests)