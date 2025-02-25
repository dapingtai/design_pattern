from abc import ABC, abstractmethod
from typing import List

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self) -> None:
        self._light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self) -> None:
        self._light.turn_off()

# Receiver
class Light:
    def turn_on(self) -> None:
        print("Light is on")

    def turn_off(self) -> None:
        print("Light is off")

# Invoker
class RemoteControl:
    def __init__(self):
        self._commands: List[Command] = []

    def add_command(self, command: Command) -> None:
        self._commands.append(command)

    def execute_commands(self) -> None:
        for command in self._commands:
            command.execute()

def main():
    # Create the receiver
    light = Light()

    # Create commands
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Create invoker and add commands
    remote = RemoteControl()
    remote.add_command(light_on)
    remote.add_command(light_off)

    # Execute all commands
    remote.execute_commands()

if __name__ == "__main__":
    main()