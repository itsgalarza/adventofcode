from src.y22.d01 import p1, p2

INPUT_DATA = "src/y22/d01/inputs/input-p1.txt"

if __name__=="__main__":
    elf_no, elf_calories =  p1.solver(INPUT_DATA)
    print(f"Elf number {elf_no} has the most calories: {elf_calories} cal")

    total_cal_top_3_elves = p2.solver(INPUT_DATA)
    print(f"The top 3 elves carrying the most cal have a total of {total_cal_top_3_elves}")
