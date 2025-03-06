import pytest
from main import main
from main import calculate_and_print

def test_main_exits(monkeypatch, capsys):
    # Mock user input
    monkeypatch.setattr('builtins.input', lambda prompt:"exit")

    with pytest.raises(SystemExit) as excinfo:
    # Run the main function
        main()

    # Optionally, check the exit status
    assert excinfo.value.code == 1


@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string",[
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "Cannot divide by zero"), # Adjusted for the actual error message
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")  # Testing another invalid number input
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string

def test_menu_command(monkeypatch, capsys):
    # Create an iterator for inputs: first "menu" then "exit"
    inputs = iter(["menu", "exit"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))

    # Run the main function (which should process "menu" and "exit")
    try:
        main()
    except SystemExit:
        # Catch SystemExit if main() exits the program after "exit"
        pass

    #Capture the output and verify that the menu is displayed
    captured = capsys.readouterr().out
    assert "Available commands:" in captured
    # Optionally check that at least one known command is listed
    assert "add" in captured
