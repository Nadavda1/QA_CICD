# tests/test_calc.py
import sys
import os

# הוספת תיקיית האב ל־sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calc import add

def test_add():
    assert add(2, 3) == 7
    assert add(-1, 1) == 0
    assert add(0, 0) == 0




