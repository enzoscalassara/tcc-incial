import pandas as pd

file1 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/py2018-6-filtered.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

# names = file1['recipient_name_raw']
names = file1['awarding_agency_name']
names_filtered = pd.Series(names)

print(set(names_filtered))

# 'recipient_name_raw'
# 'Department of Veterans Affairs', 'Department of Defense', 'National Aeronautics and Space Administration',