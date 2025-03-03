"""
Unit tests for the calculator library
"""

import os
import sys

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)

from src.utils import add, subtract, multiply, divide

class TestCalculator:

    def test_addition(self):
        assert 4 == add(2, 2)
        assert 0 == add(-1, 1)
        assert 2.5 == add(1.5, 1.0)


    def test_subtraction(self):
        assert 2 == subtract(4, 2)
        assert -1 == subtract(1, 2)
        assert 0.5 == subtract(1.5, 1.0)


    def test_multiplication(self):
        assert 6 == multiply(2, 3)
        assert 0 == multiply(0, 5)
        assert -4 == multiply(2, -2)


    def test_division(self):
        assert 2 == divide(4, 2)
        assert 2.5 == divide(5, 2)
        assert -3 == divide(6, -2)


    def test_division_by_zero(self):
        # Test that division by zero raises a ValueError
        try:
            divide(1, 0)
        except ValueError as e:
            assert str(e) == "Cannot divide by zero!"
