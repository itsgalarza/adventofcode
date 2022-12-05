from src.y22.d02 import solver

SAMPLE_DATA = 'tests/y22/d02/samples/input.txt'

def test_run_p1():
    input = solver.read_input(SAMPLE_DATA)
    res = solver.p1(input)
    assert res == 15

def test_run_p2(): 
    input = solver.read_input(SAMPLE_DATA)
    res = solver.p2(input)
    assert res == 12