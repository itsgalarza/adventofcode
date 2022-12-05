from src.y22.d05 import solver

INPUT_DATA='src/y22/d05/inputs/input.txt'

if __name__=="__main__":
    ans = solver.p1(INPUT_DATA)
    print(f"The final state after following all the instructions is: {ans}")
    ans2 = solver.p2(INPUT_DATA)
    print(f"The final state after recalculating with the new instructions: {ans2}")
