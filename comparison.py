import pandas as pd
import re
from fuzzywuzzy import fuzz
# pip install python-levenshtein
# pip install fuzzywuzzy


def clean_name(name1):

    cleaned_name = re.sub(r'[^a-zA-Z0-9\s]', '', str(name1).lower())

    return cleaned_name.strip()


def fuzzy_match(name1, name2):
    return fuzz.ratio(name1, name2)


with open("stock_market_company_names_shortened.txt", "r") as f1:
    txt_names = [line for line in f1.read().splitlines()]

with open("stock_market_company_names.txt", "r") as f5:
    txt_names_original = [line for line in f5.read().splitlines()]


f2 = pd.read_csv(filepath_or_buffer="py2018-1-filtered-agency-date-value.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')


names_original = f2['recipient_name_raw'].apply(str)
names_original = sorted(list(set(names_original)))

# names = f2['recipient_name_raw'].apply(clean_name)
# names = sorted(list(set(names)))

names = f2['recipient_name_raw'].apply(str)
names = sorted(list(set(name.lower() for name in names)))

names_list = []


for name in names:
    name = name.split()

    if len(name) > 3:
        name = "" + name[0] + " " + name[1] + " " + name[2]



complete_names_list = []

aux = 0
for name in names:

    aux_txt = 0
    for txt_name in txt_names:
        similarity = fuzzy_match(name, txt_name)

        if similarity > 80:
            names_list.append([name, similarity])
            complete_names_list.append([[name, names_original[aux]], [txt_name, txt_names_original[aux_txt]]])


        aux_txt += 1

    aux += 1

print(names_list)
print(len(names_list))


lista_final = []

for item in names_list:
    if item[0] not in lista_final:
        lista_final.append(item[0])

f3 = open("lista_final_empresas.txt", "a")
f4 = open("lista_final_empresas_para_tratamento.txt", "a")

for name in lista_final:
    f3.write(f"{name}\n")

for lista in complete_names_list:
    f4.write(f"{lista}\n")



f1.close()
f3.close()
f4.close()
f5.close()

