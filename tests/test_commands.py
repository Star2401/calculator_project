from decimal import Decimal
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_add_command():
    cmd = AddCommand()
    result = cmd.execute(Decimal('1'), Decimal('2'))
    assert result == Decimal('3')

def test_subtract_command():
    cmd = SubtractCommand()
    result = cmd.execute(Decimal('5'), Decimal('3'))
    assert result == Decimal('2')

def test_multiply_command():
    cmd = MultiplyCommand()
    result = cmd.execute(Decimal('3'), Decimal('4'))
    assert result == Decimal('12')

def test_divide_command():
    cmd = DivideCommand()
    result = cmd.execute(Decimal('10'), Decimal('2'))
    assert result == Decimal('5')
