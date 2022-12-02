from src.y22.d01 import p1, p2

SAMPLE_DATA = "tests/y22/d01/samples/d01-p1-sample.txt"

def test_run_p1():
    elf_no, calories = p1.solver(SAMPLE_DATA)
    assert calories == 24000

def test_run_p2():
    calories = p2.solver(SAMPLE_DATA)
    assert calories == 45000