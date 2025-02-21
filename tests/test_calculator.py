'''My Calculator Test'''
from calculator import Calculator
import pytest

def test_addition():
    '''Test that addition function works'''
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works'''
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that multiplication function works'''
    assert Calculator.multiply(3,2) == 6

def test_divide():
    '''Test that division function works'''
    assert Calculator.divide(2,2) == 1

def test_division_by_zero():
    '''Test that division by zero raises an error'''
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)