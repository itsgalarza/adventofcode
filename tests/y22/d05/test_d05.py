from src.y22.d05 import solver

SAMPLE_DATA = 'tests/y22/d05/samples/sample.txt'

def test_run_p1():
    stack_config, instructions = solver.read_input(SAMPLE_DATA)
    res = solver.p1(stack_config, instructions)
    assert res == 'CMZ'

def test_run_p2():
    stack_config, instructions = solver.read_input(SAMPLE_DATA)
    res = solver.p2(stack_config, instructions)
    assert res == 'MCD'