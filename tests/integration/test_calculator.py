import pytest
import os
import sys

# Ajouter la racine du projet au chemin Python
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)
from src.calculator import perform_calculation

def test_perform_calculation_addition():
    assert perform_calculation(1, 2, 3) == 5


def test_perform_calculation_subtraction():
    assert perform_calculation(2, 5, 3) == 2


def test_perform_calculation_multiplication():
    assert perform_calculation(3, 4, 2) == 8


def test_perform_calculation_division():
    assert perform_calculation(4, 10, 2) == 5


def test_perform_calculation_division_by_zero():
    assert perform_calculation(4, 10, 0) == "Cannot divide by zero!"
