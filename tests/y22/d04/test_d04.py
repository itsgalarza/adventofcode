from src.y22.d04 import solver

SAMPLE_DATA = 'tests/y22/d04/samples/sample.txt'

def test_run_p1():
    res = solver.p1(SAMPLE_DATA)
    print(res)
    assert res == 2

def test_run_p2():
    res = solver.p2(SAMPLE_DATA)
    print(res)
    assert res == 4