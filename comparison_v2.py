import ast
from fuzzywuzzy import fuzz


def fuzzy_match(name1, name2):
    return fuzz.ratio(name1, name2)


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

print(len(lista_unica))

lista_result = []

for lista in lista_unica:
    aux = 0

    for empresa in lista[1]:
        similarity = fuzzy_match(lista[0][0], empresa[0])

        if similarity > aux:
            aux = similarity
            result = empresa

    lista_result.append([lista[0], result, aux])

for i in range(1346 - 843):
    print(lista_result[i + 843])

# print(lista_result.index([['ndi engineering co', 'NDI ENGINEERING COMPANY'], ['austin engineering co', 'Austin Engineering Co. Ltd. (522005) India XBOM Industrial Machinery'], 82]))

# f2 = open("filtro_empresas_limpo.txt", "a")
# f3 = open("filtro_empresas_sujo.txt", "a")
#
# for i in range(843 - 715):
#     f2.write(f"{[lista_result[i + 715][0][1], lista_result[i + 715][1][1]]}\n")
#
# for i in range(1346 - 715):
#     f3.write(f"{[lista_result[i + 715][0][1], lista_result[i + 715][1][1]]}\n")
#
# f2.close()
# f3.close()
