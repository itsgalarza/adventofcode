from src.y22.d03.p1 import priority

def solver(input:str): 
    with open(input, encoding='utf-8', mode='r') as f:
        data = f.read().split("\n")
        data_grouped = [data[i:i+3] for i in range(0, len(data), 3)]
        badges = [list(set.intersection(*map(set,group)))[0] for group in data_grouped]
        priorities = [priority(i) for i in badges]

        return sum(priorities)