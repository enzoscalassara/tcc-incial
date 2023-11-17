import ast

with open("empresas_confirmadas.txt", "r") as f2:
    txt_names = [ast.literal_eval(line) for line in f2.read().splitlines()]

f3 = open("empresas_confirmadas_tags.txt", "a")

tags = []

for lista in txt_names:
    a = lista[0]
    b = lista[1]

    char_pos = [b.index('('), b.index(')')]

    f3.write(f"{[a, b[char_pos[0] + 1:char_pos[1]]]}\n")


f2.close()
f3.close()

