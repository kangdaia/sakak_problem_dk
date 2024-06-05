# test.py
from answer import main

def test_solution_1():
    assert main(5) == 12

def test_solution_2():
    assert main(8) == 21

def test_solution_3():
    assert main(50) == 21

def test_solution_4():
    assert main(1) == 1