# Component interface
class TextComponent:
    def format(self):
        pass


# Concrete Component
class SimpleText(TextComponent):
    def format(self):
        return "Simple Text"


# Decorator
class TextDecorator(TextComponent):
    def __init__(self, text_component):
        self._text_component = text_component

    def format(self):
        return self._text_component.format()


# Concrete Decorator 1
class BoldTextDecorator(TextDecorator):
    def format(self):
        return f"<b>{self._text_component.format()}</b>"


# Concrete Decorator 2
class ItalicTextDecorator(TextDecorator):
    def format(self):
        return f"<i>{self._text_component.format()}</i>"


# Client code
simple_text = SimpleText()
print("Original Text:", simple_text.format())

bold_text = BoldTextDecorator(simple_text)
print("Bold Text:", bold_text.format())

italic_bold_text = ItalicTextDecorator(bold_text)
print("Italic Bold Text:", italic_bold_text.format())
