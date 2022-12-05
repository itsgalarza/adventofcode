def read_input(input: str) -> list:
    with open(input, encoding='utf-8', mode='r') as f:
        data = f.read().split("\n")
    return data


def priority(char: str):
    if char.isupper():
        return ord(char) - ord('A') + 27
    return ord(char) - ord('a') + 1


def p1(data: list) -> int: 
    dup_items: list = []
    for row in data: 
        str1, str2 = row[:len(row)//2],row[len(row)//2:]
        dup_items.append([priority (i) for i in set(str1) if i in set(str2)])

    return [sum(i) for i in zip(*dup_items)][0]


def p2(data: list) -> int: 
    data_grouped = [data[i:i+3] for i in range(0, len(data), 3)]
    badges = [list(set.intersection(*map(set,group)))[0] for group in data_grouped]
    priorities = [priority(i) for i in badges]

    return sum(priorities)

