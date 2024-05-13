import os

with open("/home/qwerty/vscode/Python/EGE/ege.py") as f:
    text = f.read().strip().split("\n")

l = []
for i in range(1, 40):
    try:
        ind = text.index(f"# ЗАДАНИЕ {str(i)}")
        l.append(ind)
    except ValueError:
        pass

l.append(len(text))


print(l, len(l))
for i in range(len(l) - 1):
    num_task = text[l[i] : l[i + 1]][0].split()[-1]
    print(text[l[i] : l[i + 1]][0])
    print(num_task)
    tex = "\n".join(text[l[i] : l[i + 1]])
    new_folder = f"/home/qwerty/vscode/Python/EGE/{str(num_task)}"
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    with open(
        f"/home/qwerty/vscode/Python/EGE/{str(num_task)}/zadanie{str(num_task)}.py",
        "w",
    ) as f:
        f.write(tex)
