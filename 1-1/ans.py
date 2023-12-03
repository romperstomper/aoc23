#d={'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
d={str(x): x for x in range(1,10)}
def getleft(line):
    res=min([(line.find(x), x) for x in d if line.find(x) !=-1])
    return d[res[1]]

def getright(line):
    res=max([(line.rfind(x), x) for x in d if line.rfind(x) !=-1])
    return d[res[1]]

def combo(line):
    l=getleft(line)
    r=getright(line)
    return((l *10) + r)

def run():
    res=[]
    with open('input') as fd:
        lines=fd.readlines()
    for line in lines:
        res.append(combo(line))
    return res

if __name__ == '__main__':
    print(sum(run()))
