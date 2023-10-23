import pandas as pd

file1 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/py2018-6-filtered.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')



file_filtered = file1.loc[(file1['awarding_agency_name'] == 'Department of Defense') |
                          (file1['awarding_agency_name'] == 'National Aeronautics and Space Administration')]

file_filtered.to_csv("E:\\Ativs\\tcc\\projeto py\\py2018-6-filtered-agency.csv", index=False)




# 'Department of Defense', 'National Aeronautics and Space Administration'
