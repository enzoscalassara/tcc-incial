import pandas as pd

file1 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/py2018-1-filtered-agency.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')


file_filtered = file1.loc[(file1['total_dollars_obligated'] > 100000.00) &
                          (file1['action_date'] > '2017-10-01')]

file_filtered.to_csv("E:\\Ativs\\tcc\\projeto py\\py2018-1-filtered-agency-date-value.csv", index=False)


