from app.commands.command import Command
from calculator.operations import divide


class DivideCommand(Command):
    def execute(self, a, b):
        try:
            return divide(a, b)
        except ValuError as e:
            return str(e)