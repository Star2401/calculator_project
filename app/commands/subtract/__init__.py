from app.commands.command import Command
from calculator.operations import subtract


class SubtractCommand(Command):
    def execute(self, a, b):
        return subtract(a, b)