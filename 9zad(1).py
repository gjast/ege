with open("/home/qwerty/vscode/Python/EGE/9.txt") as f:
    text = f.read().strip()
    t = [[int(n) for n in x.split("\t")] for x in text.split("\n")]
c = 0
for i in t:
    repeat = [x for x in i if i.count(x) == 3]
    if len(repeat) >=1 and len(set(i)) == 5 and sum(i) < 502:
        c += 1
print(c)