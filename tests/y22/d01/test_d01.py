from src.y22.d01 import solver

SAMPLE_DATA = "tests/y22/d01/samples/d01-p1-sample.txt"

def test_run_p1():
    data = solver.read_input(SAMPLE_DATA)
    elf_no, calories = solver.p1(data)
    assert calories == 24000

def test_run_p2():
    data = solver.read_input(SAMPLE_DATA)
    calories = solver.p2(data)
    assert calories == 45000