"""
The Flyweight design pattern is a structural pattern 
that aims to minimize memory usage or computational expenses 
by sharing as much as possible with related objects. It is particularly 
useful when a large number of similar objects need to be created. 
The key idea is to divide the object's state into intrinsic (shared)
and extrinsic (unique) parts.
"""


class Font:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Character:
    def __init__(self, char, font):
        self.char = char
        self.font = font

    def display(self):
        print(f"Character: {self.char}, Font: {self.font.name}, Size: {self.font.size}")


class CharacterFactory:
    _character_cache = {}

    @classmethod
    def get_character(cls, char, font_name, font_size):
        key = f"{char}-{font_name}-{font_size}"
        if key not in cls._character_cache:
            font = Font(font_name, font_size)
            character = Character(char, font)
            cls._character_cache[key] = character
        return cls._character_cache[key]


# Usage
factory = CharacterFactory()

char1 = factory.get_character('A', 'Arial', 12)
char2 = factory.get_character('B', 'Times New Roman', 16)
char3 = factory.get_character('A', 'Arial', 12)  # Reuses existing 'A' character with Arial 12 font

char1.display()
char2.display()
char3.display()
