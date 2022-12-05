from src.y22.d05 import solver

SAMPLE_DATA = 'tests/y22/d05/samples/sample.txt'

def test_run_p1():
    res = solver.p1(SAMPLE_DATA)
    assert res == 'CMZ'

def test_run_p2():
    res = solver.p2(SAMPLE_DATA)
    print(res)
    assert res == 'MCD'