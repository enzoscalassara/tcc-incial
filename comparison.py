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


# f1 = open("stock_market_company_names.txt", "r")
# with open("stock_market_company_names.txt", "r") as f1:
#     txt_names = set(map(clean_name, f1.read().splitlines()))

with open("stock_market_company_names.txt", "r") as f1:
    txt_names = [clean_name(line) for line in f1.read().splitlines()]

f2 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/py2018-1-filtered-agency-date-value.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

# names = f2['recipient_name_raw'].str.lower().replace('[^a-zA-Z0-9\s]', '', regex=True)
names = f2['recipient_name_raw'].apply(clean_name)

# names = f2['recipient_name_raw']

names_list = []

# for name in set(names):
#     name_words = set(str(name).split(" "))
#
#     count = len(name_words.intersection(txt_names))
#
#     if count > 0:
#         names_list.append([name, count])

for name in set(names):
    for txt_name in txt_names:
        similarity = fuzzy_match(name, txt_name)

        if similarity > 80:
            names_list.append([name, similarity])

print(names_list)
print(len(names_list))



# names = list(set(names))

# i = 0
# for name in names:
#
#     a = str(name).split(" ")
#     for company in f1.readlines():
#
#         i = 0
#
#         for item in a:
#             if item in company:
#                 i += 1
#
#         if i > 0:
#             names_list.append([name, i])


            # --------------------------------------------


        # 'Lockheed Martin Corporation'

        # count = 0


        # for sliced_name in str(name).split(" "):
        #
        #     i += 1
        #
        #     print(sliced_name)
        #     print(i)
        #
        #     # 'Lockheed', 'Martin', 'Corporation'
        #     # 'Lockheed', 'Martin', 'Corp'
        #
        #     if sliced_name in company:
        #
        #         count += 1
        #
        # if count > 0:
        #     names_list.append([name, count])





# a = [[i, j] for i,j in names_list if j > 2]

# lista_final = []

# for elem in names_list:
#     if elem[1] > 0:
#         lista_final.append(elem)
#


#print(names_list)




f1.close()
