import pandas as pd


f1 = open("stock_market_company_names.txt", "r")

f2 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/py2018-1-filtered-agency-date-value.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

names = f2['recipient_name_raw']


names = list(set(names))

for name in names:
    for company in f1.readlines():
        if name == company:
            print(name)


f1.close()
