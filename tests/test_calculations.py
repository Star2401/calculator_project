'''My Calculator Test'''
from calculator.operations import add, multiply, subtract, divide
import pytest

def test_addition():
    '''Test that addition function works'''
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works'''
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiply works'''
    assert multiply(3,2) == 6

def test_division():
    '''Test division works'''
    assert divide(2,2) == 1

def test_division_by_zero():
    '''Test division by zero raises an error'''
    with pytest.raises(ValueError):
        divide(10,0)