import re


def clean_name(name1):

    cleaned_name = re.sub(r'[^a-zA-Z0-9\s]', '', str(name1).lower())

    return cleaned_name.strip()


f = open("stock_market_company_names_shortened.txt", "a")

with open("stock_market_company_names.txt", "r") as f1:
    txt_names = [clean_name(line) for line in f1.read().splitlines()]

for txt_name in txt_names:
    txt_name = txt_name.split()

    if len(txt_name) > 3:
        txt_name = "" + txt_name[0] + " " + txt_name[1] + " " + txt_name[2]

    f.write(f"{txt_name}\n")

f.close()
