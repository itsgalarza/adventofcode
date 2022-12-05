from src.y22.d04 import solver

INPUT_DATA = 'src/y22/d04/inputs/input.txt'

if __name__=="__main__":
    data = solver.read_input(INPUT_DATA)

    ans1 = solver.p1(data)
    print(f"The answer is: {ans1}")
    
    ans2 = solver.p2(data)
    print(f"The answer for part 2 is: {ans2}")