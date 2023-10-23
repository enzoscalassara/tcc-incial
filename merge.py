import pandas as pd

file1 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/data/py2018-1-filtered.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

file2 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/data/py2018-2-filtered.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

file3 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/data/py2018-3-filtered.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

file4 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/data/py2018-4-filtered.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

file5 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/data/py2018-5-filtered.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

file6 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/data/py2018-6-filtered.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

names1 = file1['recipient_name_raw']
names2 = file2['recipient_name_raw']
names3 = file3['recipient_name_raw']
names4 = file4['recipient_name_raw']
names5 = file5['recipient_name_raw']
names6 = file6['recipient_name_raw']

names_filtered1 = pd.Series(names1)
names_filtered2 = pd.Series(names2)
names_filtered3 = pd.Series(names3)
names_filtered4 = pd.Series(names4)
names_filtered5 = pd.Series(names5)
names_filtered6 = pd.Series(names6)


total = pd.concat([names1, names2, names3, names4, names5, names6])
total_set = set(total)

print(len(total_set))



# print(len(set(names_filtered)))

# 'recipient_name_raw'
