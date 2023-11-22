from datetime import datetime as dt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
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
        print(f"Data from file: {full_list}")

    clean_data = []

    expected_length = 6

    for data in full_list:
        if None not in data and len(data) == expected_length:
            data[0] = (dt.strptime(data[0], '%Y-%m-%d') - dt(1970, 1, 1)).days
            data[-1] = float(data[-1][:-1]) * (1e6 if 'M' in data[-1] else 1e9)
            clean_data.append(data)
        else:
            print(f"Skipping invalid data: {data}")

    clean_data = [item for item in clean_data if None not in item]

    clean_data_array = np.array(clean_data, dtype=object)


    features = np.array(clean_data_array)[:, [1, 2, 5]].astype(float)

    targets = np.array(clean_data_array)[:, 3]


    vetor1 = np.array([np.cos(np.radians(45)), np.sin(np.radians(45))])
    vetor2 = np.array([np.cos(np.radians(-15)), np.sin(np.radians(-15))])
    vetor5 = np.array([-1.0, 0.0])


    features[:, 0:2] = features[:, 0:2] * vetor1
    features[:, 2:4] = features[:, 2:4] * vetor2[:, np.newaxis]
    features[:, 4:6] = vetor5

    all_features.extend(features)
    all_targets.extend(targets)

all_features = np.array(all_features)
all_targets = np.array(all_targets)

X_train, X_test, y_train, y_test = train_test_split(all_features, all_targets, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


model = RandomForestRegressor(n_estimators=100, random_state=42)


model.fit(X_train, y_train)


predictions = model.predict(X_test)


mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')


result_df = pd.DataFrame({
    'Actual Stock Price Change': y_test,
    'Predicted Stock Price Change': predictions,
})

pd.set_option('display.max_columns', None)


print(result_df)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(y_test, predictions)
plt.xlabel("Actual Stock Price Change")
plt.ylabel("Predicted Stock Price Change")
plt.title("Actual vs. Predicted Stock Price Change")

plt.tight_layout()
plt.show()
