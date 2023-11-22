import datetime as dt
import pandas as pd
import ast
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



def check_marketcap(tag, data):

    data = data.split('-')
    data[1] = int(data[1])

    if 7 < data[1] < 11:
        data[1] = 9

    elif 4 < data[1] < 8:
        data[1] = 6

    elif 1 < data[1] < 5:
        data[1] = 3

    else:
        data[1] = 1



    # data = f"{data[1]}/{data[2]}/{data[0]}"


    options = Options()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options)

    driver.get(f'https://www.marketcaphistory.com/?symbol={tag}')

    # Data vem no formato AAAA-MM-DD
    # No site está MM-DD-AAAA
    # Primeiro eu analiso o ano
    # Depois eu comparo o mes para ser igual


    table = driver.find_elements(By.XPATH, '/html/body/center/div[4]/div[2]/div[2]/table[1]/tbody/tr[2]/td/center/table/tbody/tr')

    for row in table:
        cells = row.find_elements(By.TAG_NAME, 'td')
        # print(str(cells[0].text)[5:])
        # print(str(data[0]))

        # print(f"1 - {str(cells[0].text)[1]}")
        # print(f"Meu - {str(data[1])}")

        if str(cells[0].text)[5:] == str(data[0]) and str(cells[0].text)[0] == str(data[1]):
            return cells[1].text




check_marketcap("ABT", "2020-01-01")
