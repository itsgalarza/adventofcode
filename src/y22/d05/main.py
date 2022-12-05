from src.y22.d05 import solver

INPUT_DATA='src/y22/d05/inputs/input.txt'

if __name__=="__main__":
    stack_config, instructions = solver.read_input(INPUT_DATA)

    ans = solver.p1(stack_config, instructions)
    print(f"The final state after following all the instructions is: {ans}")
    ans2 = solver.p2(stack_config, instructions)
    print(f"The final state after recalculating with the new instructions: {ans2}")
