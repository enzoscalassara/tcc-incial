from datetime import datetime as dt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
import ast
import matplotlib.pyplot as plt
import os

from index_values import index_values

data_directory = "Dados_Funcionais_Clean"

# Lists to store data from all files
all_features = []
all_targets = []

# Loop through all files in the directory
for filename in os.listdir(data_directory):
    file_path = os.path.join(data_directory, filename)

    with open(file_path, "r") as f:
        print(f"Processing file: {file_path}")
        full_list = [ast.literal_eval(line) for line in f.read().splitlines()]

    clean_data = []

    expected_length = 6

    for data in full_list:
        if float(data[2]) > 280 and None not in data and len(data) == expected_length:

            data[-1] = float(data[-1][:-1]) * (1e6 if 'M' in data[-1] else 1e9)
            var7d, var3m = index_values(data[0])
            data.append(var7d)
            data.append(var3m)
            data[0] = (dt.strptime(data[0], '%Y-%m-%d') - dt(1970, 1, 1)).days
            clean_data.append(data)
        else:
            pass

    clean_data_array = np.array(clean_data)

    # Extract relevant columns for features and targets
    if len(clean_data_array) > 0:
        features = np.array(clean_data_array)[:, [1, 2, 5, 6, 7]]
        targets = np.array(clean_data_array)[:, 3]

        all_features.extend(features)
        all_targets.extend(targets)

all_features = np.array(all_features)
all_targets = np.array(all_targets)

ranges = [(280.0, 400.0)]

features_ranges = []
targets_ranges = []


for start, end in ranges:


    mask = np.array([float(feature[1]) >= start and float(feature[1]) <= end for feature in all_features])
    features_range = all_features[mask]
    targets_range = all_targets[mask]


    # Split the combined data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        features_range, targets_range, test_size=0.1, random_state=43
    )


    # Initialize the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    mea = mean_absolute_error(y_test, predictions)
    print(f'Mean Squared Error for all ranges: {mse}')
    print(f'Mean Absolute Error for all ranges: {mea}')

    result_df = pd.DataFrame({
        'Predicted 7 days after': predictions,
        'Actual 7 days after': y_test,

    })

    result_df2 = pd.DataFrame({
        '7 days before': X_test[:, 0],
        'Predicted 7 days after': X_test[:, 1],
        'Actual 7 days after': X_test[:, 2],

    })

    pd.set_option('display.max_columns', None)

    # Display the table
    print(result_df)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.scatter(y_test, predictions)
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Actual vs. Predicted Values for all ranges")
    plt.show()
