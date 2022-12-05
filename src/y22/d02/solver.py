

shape_score = {
    'X':1,
    'Y':2,
    'Z':3
}

wins = {
    'A':'Y',
    'B':'Z',
    'C':'X'
}

draws = {
    'A':'X',
    'B':'Y',
    'C':'Z'
}

loses = {
    'A':'Z',
    'B':'X',
    'C':'Y'
}

draws_list = [[k,v] for k,v in draws.items()]
wins_list = [[k,v] for k,v in wins.items()]

def read_input(input:str) -> list:
        with open(input, encoding='utf-8', mode='r') as f:
         lines = list()
         for line in f.readlines():
             lines.append(line.split())
        
        return lines


def p1(lines: list) -> int:
    score = 0
    for l in lines:
        score += (l in draws_list) * 3
        score += (l in wins_list) * 6
        score += shape_score[l[1]]
    
    return score


def p2(lines: list) -> int:
    for i, line in enumerate(lines):
        opponent, result = list(line)
        if result == 'X':
            lines[i][1] = loses[opponent]
        elif result == 'Y':
            lines[i][1] = draws[opponent]
        else:
            lines[i][1] = wins[opponent]
    
    return p1(lines)


