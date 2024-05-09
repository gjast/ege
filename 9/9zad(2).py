from itertools import *
with open("/home/qwerty/vscode/Python/EGE/9(1).txt") as f:
    text = f.read().strip()
    t = [sorted([int(i) for i in x.split("\t")]) for x in text.split("\n")]
c = 0
for i in t:
    su = [x for x in i[:-1]]
    l = [j for j in permutations(i, 4) if (j[0] + j[1]) != (j[2] + j[3])]
    if i[-1] < sum(su) and len(l) == 24:
        c += 1
print(c)
