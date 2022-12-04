from src.y22.d03 import p1, p2

INPUT_DATA = "src/y22/d03/inputs/input.txt"

if __name__=="__main__":
    res = p1.solver(INPUT_DATA)
    print(f"The sum of priorities is {res}")
    res2 = p2.solver(INPUT_DATA)
    print(f"The result of the agg from the badges is: {res2}")
