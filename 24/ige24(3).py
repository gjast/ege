with open("/home/qwerty/vscode/Python/EGE/24(3).txt") as f:
    text = f.read()
    for i in range(10):
        text = text.replace(str(i), "2" if i % 2 == 0 else "1")
    text = text.replace("1", "1 1").replace("2", "2 2").split()
l = []
for i in range(len(text)):
    if (text[i][0].isdigit() and text[i][-1].isdigit()) and (text[i][0] != text[i][-1]):
        l.append(len(text[i]))
print(max(l))
