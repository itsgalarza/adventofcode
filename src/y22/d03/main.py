from src.y22.d03 import solver

INPUT_DATA = "src/y22/d03/inputs/input.txt"

if __name__=="__main__":
    data = solver.read_input(INPUT_DATA)

    res = solver.p1(data)
    print(f"The sum of priorities is {res}")
    
    res2 = solver.p2(data)
    print(f"The result of the agg from the badges is: {res2}")
