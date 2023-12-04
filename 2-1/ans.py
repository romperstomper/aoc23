import re
def getcubes(line):
    res = []
    for x in line.split(';'):
        games = re.findall(r'(\d+ \w+)', x)
        d=dict(y.split(' ')[::-1] for y in games)
        nd=dict((k, int(v)) for (k, v) in d.items())
        res.append(nd)
    return res

def checksub(sub):
    static = {'red': 12, 'green': 13, 'blue': 14}
    for k in sub:
        if sub[k] > static[k]:
            print(static[k], sub[k])
            return False
    return True

def run():
    c=0
    res=0
    with open('input') as fd:
        lines=fd.readlines()
    for line in lines:
        c+=1
        cubes=getcubes(line)
        print(cubes)
        tmp=[]
        for sub in cubes:
            tmp.append(checksub(sub))
        if all(tmp):
            res +=c
        print(False, tmp)
    return res

if __name__ == '__main__':
    print(run())
