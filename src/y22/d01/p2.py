from src.y22.d01.p1 import get_sorted_elves

def solver(input: str):
    with open(input, encoding='utf-8', mode='r') as f:
        data = f.read().split("\n\n")
        item_cal_per_elf, sorted_elves = get_sorted_elves(data)

        return sum([sum(i) for i in sorted_elves[-3::]])