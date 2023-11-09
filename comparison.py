import pandas as pd


f1 = open("stock_market_company_names.txt", "r")

f2 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/py2018-1-filtered-agency-date-value.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

names = f2['recipient_name_raw']

names_list = []

names = list(set(names))

for name in names:

    count = 0
    for sliced_name in str(name):
        print(sliced_name)
        for company in f1.readlines():
            if sliced_name in company:
                count += 1

    names_list.append([name, count])

# a = [[i, j] for i,j in names_list if j > 2]

lista_final = []

for elem in names_list:
    if elem[1] > 0:
        lista_final.append(elem)

print(lista_final)




f1.close()
