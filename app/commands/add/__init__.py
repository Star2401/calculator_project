from app.commands.command import Command
from calculator.operations import add


class AddCommand(Command):
    def execute(self, a, b):
        return add(a, b)
