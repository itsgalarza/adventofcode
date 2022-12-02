def get_sorted_elves(data):
    calories_per_elf = [tuple(map(int, elf.splitlines())) for elf in data]
    sorted_elves = sorted(calories_per_elf, key=sum)

    return calories_per_elf, sorted_elves


def solver(input: str): 
    with open(input, encoding='utf-8', mode='r') as f:
        data = f.read().split("\n\n")
        item_cal_per_elf, sorted_elves = get_sorted_elves(data)

        elf_no = item_cal_per_elf.index(sorted_elves[-1])
        elf_calories = sum(sorted_elves[-1])

        return elf_no, elf_calories

