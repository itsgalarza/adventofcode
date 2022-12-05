from src.y22.d02 import solver


INPUT_DATA = "src/y22/d02/inputs/input.csv"


if __name__=="__main__":
    input = solver.read_input(INPUT_DATA)

    hypothetical_scoring = solver.p1(input)
    print(f"Guessing our hypothesis is right, we'll be scoring {hypothetical_scoring} points")

    final_scoring = solver.p2(input)
    print(f"Following the given rules, we'd score: {final_scoring}")

