import pandas as pd
import ast


f1 = pd.read_csv(filepath_or_buffer="py2018-1-filtered-agency-date-value.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

names = f1['recipient_name_raw'].apply(str)

with open("empresas_confirmadas.txt", "r") as f2:
    txt_names = [ast.literal_eval(line) for line in f2.read().splitlines()]

# print(txt_names[0][0])
NAME = txt_names[0][0]


mask = names.apply(lambda x: NAME in x)

filtered_rows = f1[mask]
a = filtered_rows[['total_dollars_obligated', 'multi_year_contract', 'action_date', 'last_modified_date']].groupby(['action_date']).mean()
print(filtered_rows[['total_dollars_obligated', 'multi_year_contract', 'action_date', 'last_modified_date']].groupby(['action_date']).mean())
# filtered_rows[['total_dollars_obligated', 'multi_year_contract', 'action_date', 'last_modified_date']].to_csv("abbott_labs.csv", index=False)


f2.close()

# ['2017-10-30', 8637244.02, 56.21, 55.32, 23658.84, 24128,07, 92.88]
# [data-do-contrato, valor-do-contrato, valor-da-ação-7-dias-antes, valor-da-ação-7-dias-depois, índice-do-setor-1-mes-e-meio-antes, índice-do-setor-1-mes-e-meio-depois, market-cap]

# data-do-contrato, valor-do-contrato  ====  pandas
# valor-da-ação-7-dias-antes, valor-da-ação-7-dias-depois   =====  yahoo finance
# índice-do-setor-1-mes-e-meio-antes, índice-do-setor-1-mes-e-meio-depois  =====  spglobal
# market cap no mes mais proximo (1, 3, 9)  =====  market cap





