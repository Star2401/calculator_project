"""Command line calculator application that performs basic arithmetic operations.

This module provides a command-line interface for performing calculations
using decimal numbers. It supports basic operations like addition, subtraction,
multiplication, and division.
"""

import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator
from app import App

# You have to include this in your main.py because this forces the program to start when you run it from the command line.
if __name__ == "__main__":
    app = App().start() # Instantiate an instance of App

class OperationCommand:
    """Implements the Command pattern for calculator operations.
    
    This class encapsulates all the information needed to perform a calculation
    operation at a later time.
    
    Attributes:
        calculator: The calculator class to use for operations
        operation_name: Name of the operation to perform (add, subtract, etc.)
        a: First decimal number
        b: Second decimal number
    """
    
    def __init__(self, calculator, operation_name, a, b):
        """Initialize the command with calculator and operation details.

        Args:
            calculator: Calculator class to use
            operation_name: String name of operation
            a: First decimal number
            b: Second decimal number
        """
        self.calculator = calculator
        self.operation_name = operation_name
        self.a = a
        self.b = b

    def execute(self):
        operation_method = getattr(self.calculator, self.operation_name, None)
        if not operation_method:
            raise ValueError(f"Unknown operation: {self.operation_name}")
        return operation_method(self.a, self.b)

def calculate_and_print(a, b, operation_name):
    """Calculate and print the result"""
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command = OperationCommand(Calculator, operation_name, a_decimal, b_decimal)
        result = command.execute()
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print(f"Error: Division by zero.")
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Entry point for the calculator application."""
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation_name = sys.argv
    calculate_and_print(a, b, operation_name)

if __name__ == '__main__':
    main()


