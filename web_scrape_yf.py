import datetime as dt
import pandas as pd
import ast
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dateutil.relativedelta import relativedelta
from web_scrape_marketcap import check_marketcap
import time


def check_params_data(data_do_contrato):
    data_zero = dt.datetime(1970, 1, 1)
    # 2017-10-30
    data_do_contrato = data_do_contrato.split('-')
    data_do_contrato = [int(i) for i in data_do_contrato]

    data_do_contrato = dt.datetime(data_do_contrato[0], data_do_contrato[1], data_do_contrato[2])

    range_sete_dias = (7 * 86400)

    data_3_meses = data_do_contrato + relativedelta(months=3)



    query_p1 = (data_do_contrato - data_zero).total_seconds() - range_sete_dias
    query_p2 = (data_3_meses - data_zero).total_seconds()



    return [int(query_p1), int(query_p2)]


def check_url(tag, query_p1, query_p2):
    url = f'https://finance.yahoo.com/quote/{tag}/history?period1={query_p1}&period2={query_p2}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
    return url


f1 = pd.read_csv(filepath_or_buffer="py2018-1-filtered-agency-date-value.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

names = f1['recipient_name_raw'].apply(str)

with open("empresas_confirmadas_tags.txt", "r") as f2:
    txt_names = [ast.literal_eval(line) for line in f2.read().splitlines()]

options = Options()
options.add_argument('--headless')
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options)

counter = 0


for j in range(55, len(txt_names)):
    NAME = txt_names[j][0]
    tag = txt_names[j][1]

    print(f"{NAME} - {tag} - {j}")

    f3 = open(f"Dados/{tag}.txt", "a")

    mask = names.apply(lambda x: NAME in x)

    filtered_rows = f1[mask]

    # start = time.time()

    a = list(filtered_rows['total_dollars_obligated'])
    b = list(filtered_rows['action_date'])

    c = []
    for i in range(len(a)):
        counter += 1
        c.append([b[i], a[i]])

    c.sort(key=lambda x: x[0])

    for i in range(len(c)):


        data_do_contrato = str(c[i][0])

        print(i)



        params = check_params_data(data_do_contrato)

        url = check_url(tag, params[0], params[1])


        driver.get(url)
        table = driver.find_elements(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr')

        if len(table) < 1:
            pass
        else:
            row1 = table[-1].find_elements(By.TAG_NAME, 'td')
            if len(row1) < 7:
                row1 = table[-2].find_elements(By.TAG_NAME, 'td')
            row2 = table[-15].find_elements(By.TAG_NAME, 'td')
            if len(row2) < 7:
                row2 = table[-16].find_elements(By.TAG_NAME, 'td')
            row3 = table[0].find_elements(By.TAG_NAME, 'td')
            if len(row3) < 7:
                row3 = table[1].find_elements(By.TAG_NAME, 'td')

            marketcap = check_marketcap(tag, data_do_contrato)

            f3.write(f"{[data_do_contrato, c[i][1], row1[2].text, row2[2].text, row3[2].text, marketcap]}\n")

        # end = time.time()
        # print(end - start)


    f3.close()

print(counter)

f2.close()
# Write o que está abaixo no arquivo, para cada contrato
# [data-do-contrato, valor-do-contrato, valor-da-ação-7-dias-antes, valor-da-ação-7-dias-depois, valor-da-ação-3-meses-depois, market-cap]
