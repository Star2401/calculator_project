from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class CommandHandler:
    def __init__(self):
        # Map command names to their corresponding command objects
        self.commands = {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "multiply": MultiplyCommand(),
            "divide": DivideCommand()
        }

    def execute(self, command_name: str, a: float, b: float):
        # Retrieve the command from the dictionary
        command = self.commands.get(command_name.lower())
        if not command:
            raise ValueError(f"Unknown command: {command_name}")
        # Execute the command with the provided arguments
        return command.execute(a,b)