import ast
from fuzzywuzzy import fuzz


with open("lista_final_empresas_para_tratamento.txt", "r") as f1:
    txt_names = [ast.literal_eval(line) for line in f1.read().splitlines()]





lista_unica = []
lista_unica.append([txt_names[0][0], []])

aux = -1
i = 0
for lista in txt_names:
    if lista[0] not in lista_unica[i]:
        lista_unica.append([lista[0], [lista[1]]])
        aux += 1
        i += 1

    else:
        lista_unica[aux][1].append(lista[1])

print(lista_unica[4])

for lista in lista_unica:
    pass
