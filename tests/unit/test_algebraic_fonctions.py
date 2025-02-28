""" 
Unit tests for the calculator library 
""" 

# tests/unit/test_algebraic_functions.py
import os
import sys

# Ajouter le répertoire racine du projet au chemin Python
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.insert(0, project_root)

from utils import add, subtract, multiply, divide

class TestCalculator:
    def test_addition(self):
        assert add(2, 2) == 4

    def test_subtraction(self):
        assert subtract(4, 2) == 2

    def test_multiplication(self):
        assert multiply(3, 4) == 12

    def test_division(self):
        assert divide(10, 2) == 5

    def test_division_by_zero(self):
        try:
            divide(10, 0)
        except ValueError as e:
            assert str(e) == "Cannot divide by zero"
            