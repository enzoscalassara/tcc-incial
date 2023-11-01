from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

f = open("stock_market_company_names.txt", "a")

driver = webdriver.Chrome(options=options)

for page in range(2):

    driver.get(f"https://www.wsj.com/market-data/quotes/company-list/a-z/0-9/{page + 1}")

    all_links = driver.find_elements(By.CLASS_NAME, 'cl-name')

    for elem in all_links:
        f.write(f"{elem.text}\n")


alphabet = [['a', 37], ['b', 23], ['c', 33], ['d', 14], ['e', 17], ['f', 14], ['g', 19], ['h', 18], ['i', 15],
            ['j', 9], ['k', 13], ['l', 12], ['m', 23], ['n', 17], ['o', 9], ['p', 20], ['q', 3], ['r', 13], ['s', 45],
            ['t', 22], ['u', 6], ['v', 9], ['w', 9], ['x', 3], ['y', 4], ['z', 6], ['Other', 1]]

for item in alphabet:
    for page in range(item[1]):

        driver.get(f"https://www.wsj.com/market-data/quotes/company-list/a-z/{item[0].upper()}/{page + 1}")

        all_links = driver.find_elements(By.CLASS_NAME, 'cl-name')

        for elem in all_links:

            f.write(f"{elem.text}\n")

f.close()

driver.quit()

