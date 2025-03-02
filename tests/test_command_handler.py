from decimal import Decimal
import pytest
from app.command_handler import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_register_and_execute():
    handler = CommandHandler()
    # Register commands
    handler.register_command("add", AddCommand())
    handler.register_command("subtract", SubtractCommand())
    handler.register_command("multiply", MultiplyCommand())
    handler.register_command("divide", DivideCommand())

    # Execute commands and check results
    result_add = handler.execute("add", Decimal('2'), Decimal('3'))
    result_sub = handler.execute("subtract", Decimal('5'), Decimal('3'))
    result_mul = handler.execute("multiply", Decimal('3'), Decimal('4'))
    result_div = handler.execute("divide", Decimal('10'), Decimal('2'))

    assert result_add == Decimal('5')
    assert result_sub == Decimal('2')
    assert result_mul == Decimal('12')
    assert result_div == Decimal('5')

def test_unknown_command():
    handler = CommandHandler()
    with pytest.raises(ValueError):
        handler.execute("unknown", Decimal('2'), Decimal('3'))
    