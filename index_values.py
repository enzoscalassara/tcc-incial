import pandas as pd
from datetime import datetime as dt, timedelta
from dateutil.relativedelta import relativedelta


def index_values(date):
    f1 = pd.read_csv(filepath_or_buffer="Dados/index.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

    dates = f1['Date'].apply(str)

    # '2018-07-10'
    date_clean = dt.strptime(date, '%Y-%m-%d')

    date_atual = date_clean
    date_atual_formatted = date_clean.strftime('%m/%d/%Y')
    date_atual_formatted = '/'.join(part.lstrip('0') for part in date_atual_formatted.split('/'))
    valor_atual = f1.loc[dates == date_atual_formatted, 'Index']
    while valor_atual.empty:
        date_atual = date_atual + timedelta(days=1)
        date_atual_formatted = date_atual.strftime('%m/%d/%Y')
        date_atual_formatted = '/'.join(part.lstrip('0') for part in date_atual_formatted.split('/'))
        valor_atual = f1.loc[dates == date_atual_formatted, 'Index']


    date_7_antes = date_clean - timedelta(days=7)
    date_7_antes_formatted = date_7_antes.strftime('%m/%d/%Y')
    date_7_antes_formatted = '/'.join(part.lstrip('0') for part in date_7_antes_formatted.split('/'))
    valor_7d = f1.loc[dates == date_7_antes_formatted, 'Index']
    while valor_7d.empty:
        date_7_antes = date_7_antes - timedelta(days=1)
        date_7_antes_formatted = date_7_antes.strftime('%m/%d/%Y')
        date_7_antes_formatted = '/'.join(part.lstrip('0') for part in date_7_antes_formatted.split('/'))
        valor_7d = f1.loc[dates == date_7_antes_formatted, 'Index']

    date_3_meses_antes = date_clean - relativedelta(months=3)
    date_3_meses_antes_formatted = date_3_meses_antes.strftime('%m/%d/%Y')
    date_3_meses_antes_formatted = '/'.join(part.lstrip('0') for part in date_3_meses_antes_formatted.split('/'))
    valor_3m = f1.loc[dates == date_3_meses_antes_formatted, 'Index']
    while valor_3m.empty:
        date_3_meses_antes = date_3_meses_antes - timedelta(days=1)
        date_3_meses_antes_formatted = date_3_meses_antes.strftime('%m/%d/%Y')
        date_3_meses_antes_formatted = '/'.join(part.lstrip('0') for part in date_3_meses_antes_formatted.split('/'))
        valor_3m = f1.loc[dates == date_3_meses_antes_formatted, 'Index']

    valor_atual = float(valor_atual.iloc[0].replace(',', '.'))
    valor_7d = float(valor_7d.iloc[0].replace(',', '.'))
    valor_3m = float(valor_3m.iloc[0].replace(',', '.'))

    var_7d = valor_atual / valor_7d
    var_3m = valor_atual / valor_3m

    return var_7d, var_3m


