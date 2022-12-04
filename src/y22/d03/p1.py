def priority(char: str):
    if char.isupper():
        return ord(char) - ord('A') + 27
    return ord(char) - ord('a') + 1

def solver(input:str): 
    with open(input, encoding='utf-8', mode='r') as f:
        data = f.read().split("\n")
        print(data)
        dup_items: list = []
        for row in data: 
            str1, str2 = row[:len(row)//2],row[len(row)//2:]
            dup_items.append([priority (i) for i in set(str1) if i in set(str2)])

        return [sum(i) for i in zip(*dup_items)][0]
