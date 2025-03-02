from app.commands.command import Command
from calculator.operations import multiply


class MultiplyCommand(Command):
    def execute(self, a, b):
        return multiply(a, b)
