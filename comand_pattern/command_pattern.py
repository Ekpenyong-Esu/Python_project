"""
the Command pattern is another behavioral design pattern that 
encapsulates a request as an object, thereby allowing parameterization 
of clients with queues, requests, and operations. This pattern allows for 
the separation of concerns between sender and receiver.
"""


from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    
    @abstractmethod
    def execute(self):
        pass

# Receiver
class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

# Concrete Command
class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

# Concrete Command
class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Invoker
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command):
        self.commands[command_name] = command

    def execute_command(self, command_name):
        command = self.commands.get(command_name)
        if command:
            command.execute()
        else:
            print("Command not found")

# Client code
if __name__ == "__main__":
    # Receiver
    light = Light()

    # Concrete Commands
    turn_on_command = TurnOnCommand(light)
    turn_off_command = TurnOffCommand(light)

    # Invoker
    remote_control = RemoteControl()
    remote_control.register_command("on", turn_on_command)
    remote_control.register_command("off", turn_off_command)

    # Client sends requests
    remote_control.execute_command("on")
    remote_control.execute_command("off")
