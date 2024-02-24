"""
The Proxy pattern is a structural design pattern that provides a surrogate or a 
placeholder for another object to control access to it. This pattern involves a proxy class, 
which acts as an intermediary, controlling access to the real object.
"""
from abc import ABC, abstractmethod

# Subject Interface
class Image(ABC):
    
    @abstractmethod
    def display(self):
        pass

# Real Subject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image from file: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")

# Proxy
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Client Code
if __name__ == "__main__":
    # Using RealImage directly
    real_image = RealImage("example.jpg")
    real_image.display()

    # Using ProxyImage
    proxy_image = ProxyImage("example.jpg")
    proxy_image.display()
