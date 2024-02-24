import abc

class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class AnimalFactory:
    def get_animal(self, type):
        if type == "dog":
            return Dog()
        elif type == "cat":
            return Cat()
        else:
            return None

if __name__ == "__main__":
    factory = AnimalFactory()
    animal = factory.get_animal("dog")
    animal.speak()