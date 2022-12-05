import re
from typing import Tuple

def read_input(input:str) -> Tuple[str, str]:
    with open(input, encoding='utf-8', mode='r') as f:
        stack_config, instructions = f.read().split("\n\n")
    return stack_config, instructions


def read_stack_config(stack_config: str) -> list: 
    stack_conf_by_line = stack_config.split("\n")
    
    no_stacks = int(re.findall(r'\d+', stack_conf_by_line[-1])[-1])
    stacks = [[] for i in range(no_stacks)]

    for line in stack_conf_by_line[:-1][::-1]:
        for i in list(range(no_stacks)):
            # items are in position (i+(i+1))*2 of the string, -1 for quote char
            item = line[(4*i+1)]
            stacks[i].append(item) if item!= ' ' else stacks[i]

    return stacks


def operations(instructions: str, stacks):
     
    instruction_lines = instructions.splitlines()
    for line in instruction_lines:
        _, _number, _, _from, _, _to = line.split(" ")
        for i in range(int(_number)):
            moving = stacks[int(_from)-1][-1]
            stacks[int(_to)-1].append(moving)
            stacks[int(_from)-1].pop()

    return stacks

def get_final_state(stacks):
    res: str =''
    for stack in stacks:
        res += stack[-1]
    
    return res


def cratemover_9001(instructions: str, stacks):
    instruction_lines = instructions.splitlines()
    for line in instruction_lines:
        _, _number, _, _from, _, _to = line.split(" ")
        bulk_moving = stacks[int(_from)-1][-int(_number):][::-1]
        for i in bulk_moving[::-1]:
            stacks[int(_to)-1].append(i)
            stacks[int(_from)-1].pop()

    return stacks


def p1(stack_config: str, instructions: str):
    
    stacks = read_stack_config(stack_config)
    result = operations(instructions, stacks)
    ans = get_final_state(result)
    return ans


def p2(stack_config: str, instructions: str):
 
    stacks = read_stack_config(stack_config)
    result = cratemover_9001(instructions, stacks)
    ans = get_final_state(result)
    return ans
