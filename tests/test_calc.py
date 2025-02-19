# tests/test_calc.py
import sys
import os

# הוספת תיקיית האב ל־sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from calc import add
from calc import sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(7, 20) == 27

def test_sub():
    assert sub(2,2) == 0




