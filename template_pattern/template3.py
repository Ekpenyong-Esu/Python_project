from abc import ABC, abstractmethod

class Game(ABC):

    def template_method(self):
        self.initialize()
        self.start_play()
        self.end_play()

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def start_play(self):
        pass

    @abstractmethod
    def end_play(self):
        pass

class Chess(Game):
    
    def initialize(self):
        print("Setting up chess board")

    def start_play(self):
        print("Start playing chess")

    def end_play(self):
        print("End chess game")

class Monopoly(Game):

    def initialize(self):
        print("Setting up monopoly board")

    def start_play(self):
        print("Start playing monopoly")

    def end_play(self):
        print("End monopoly game")
        
def main():
    game1 = Chess()
    game1.template_method()

    game2 = Monopoly()
    game2.template_method()

if __name__ == "__main__":
    main()