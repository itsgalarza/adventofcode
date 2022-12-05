from src.y22.d03 import solver

SAMPLE_DATA = 'tests/y22/d03/samples/sample.txt'


def test_run_p1():
    data = solver.read_input(SAMPLE_DATA)
    res = solver.p1(data)
    assert res == 157

def test_run_p2():
    data = solver.read_input(SAMPLE_DATA)
    res = solver.p2(data)
    assert res == 70