from datetime import datetime as dt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import ast
import matplotlib.pyplot as plt
import os


data_directory = "Dados_Funcionais_Clean"


all_features = []
all_targets = []

for filename in os.listdir(data_directory):
    file_path = os.path.join(data_directory, filename)

    with open(file_path, "r") as f:
        print(f"Processing file: {file_path}")
        full_list = [ast.literal_eval(line) for line in f.read().splitlines()]

    clean_data = []

    expected_length = 6

    for data in full_list:
        if None not in data and len(data) == expected_length:
            data[0] = (dt.strptime(data[0], '%Y-%m-%d') - dt(1970, 1, 1)).days
            data[-1] = float(data[-1][:-1]) * (1e6 if 'M' in data[-1] else 1e9)
            clean_data.append(data)
        else:
            pass

    clean_data_array = np.array(clean_data)

    features = np.array(clean_data_array)[:, [1, 2, 5]]
    targets = np.array(clean_data_array)[:, 3]

    all_features.extend(features)
    all_targets.extend(targets)

all_features = np.array(all_features)
all_targets = np.array(all_targets)

ranges = [(0.0, 120.0), (120.0, 180.0), (300.0, 400.0)]

features_ranges = []
targets_ranges = []

tabela = 0
for start, end in ranges:


    mask = np.array([float(feature[1]) >= start and float(feature[1]) <= end for feature in all_features])
    features_range = all_features[mask]
    targets_range = all_targets[mask]



    X_train, X_test, y_train, y_test = train_test_split(
        features_range, targets_range, test_size=0.5, random_state=54
    )



    model = RandomForestRegressor(n_estimators=100, random_state=54)


    model.fit(X_train, y_train)


    predictions = model.predict(X_test)


    mse = mean_squared_error(y_test, predictions)
    mea = mean_absolute_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')
    print(f'Mean Absolute Error: {mea}')

    y_test = y_test.astype(float)

    result_df = pd.DataFrame({
        'Valor 7 Dias Antes': X_test[:, 1],
        'Valor Estimado': predictions,
        'Valor Real': y_test,
        'Diferença Absoluta': np.round(np.abs(predictions - y_test), 4)
    })

    result_df.to_excel(f'Tabelas_Resultados/tabela_{tabela}.xlsx', index=False)
    tabela += 1


    pd.set_option('display.max_columns', None)


    print(result_df)



    plt.figure(figsize=(12, 6))
    plt.scatter(y_test, predictions)
    plt.xlabel("Valor Real")
    plt.ylabel("Valor Estimado")
    plt.title("Valor Real vs. Valor Estimado")
    plt.xticks(np.linspace(min(y_test), max(y_test), 10))
    plt.show()
