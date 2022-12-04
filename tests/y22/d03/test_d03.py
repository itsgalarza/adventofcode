from src.y22.d03 import p1, p2

SAMPLE_DATA = 'tests/y22/d03/samples/sample.txt'


def test_run_p1():
    res = p1.solver(SAMPLE_DATA)
    assert res == 157

def test_run_p2():
    res = p2.solver(SAMPLE_DATA)
    assert res == 70