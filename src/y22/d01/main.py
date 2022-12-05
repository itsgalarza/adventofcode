from src.y22.d01 import solver

INPUT_DATA = "src/y22/d01/inputs/input-p1.txt"

if __name__=="__main__":
    data = solver.read_input(INPUT_DATA)

    elf_no, elf_calories =  solver.p1(data)
    print(f"Elf number {elf_no} has the most calories: {elf_calories} cal")

    total_cal_top_3_elves = solver.p2(data)
    print(f"The top 3 elves carrying the most cal have a total of {total_cal_top_3_elves}")
