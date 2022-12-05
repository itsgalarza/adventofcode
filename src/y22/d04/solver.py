

def get_ranges(single_limit: str):
    limit = sorted([int(i) for i in single_limit.split("-")])
    rge = [*range(limit[0], limit[1]+1)]
    return rge



def p1(input: str):
    with open(input, encoding='utf-8', mode='r') as f:
        data = f.read().split("\n")
        l = list()
        
        for pair in data:
            
            splitted = pair.split(",")
            rge1 = get_ranges(splitted[0])
            rge2 = get_ranges(splitted[1])          

            if len(rge1)>len(rge2):
                l.append(1) if (rge1[0]<=rge2[0] and rge1[-1]>=rge2[-1]) else l
            elif len(rge2)>len(rge1):
                l.append(1) if (rge2[0]<=rge1[0] and rge2[-1]>=rge1[-1]) else l
            else:
                l.append(1) if rge1==rge2 else l
            
        return sum(l)

                
def p2(input: str): 
    with open(input, encoding='utf-8', mode='r') as f:
        data = f.read().split("\n")
        l = list()
        for pair in data:
            splitted = pair.split(",")
            rge1 = set(get_ranges(splitted[0]))
            rge2 = set(get_ranges(splitted[1]))
            l.append(1) if len(rge1.intersection(rge2))>0 else l
        
        return sum(l)

        