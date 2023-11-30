
import pandas as pd
import numpy as np

# Parameters
n_rows = 12
n_cols = 8  # A to H
n_groups = 10
n_replicates = 5
time_intervals = 10  # minutes
total_duration = 16 * 60  # 16 hours in minutes
measurement_times = np.arange(0, total_duration + time_intervals, time_intervals)

# Creating a mapping for well positions
columns_map = {index: letter for index, letter in enumerate("ABCDEFGH", start=1)}
rows_map = {index: str(index) for index in range(1, n_rows + 1)}

# Redefining the function to adjust the output format
def simulate_growth_data_pivot():
    data = []
    for group in range(1, n_groups + 1):
        for replicate in range(1, n_replicates + 1):
            row = group + 1  # Rows start from 2
            col = replicate + 2  # Columns start from C
            well_id = columns_map[col] + rows_map[row]
            growth_measurements = np.random.normal(loc=0.5, scale=0.1, size=len(measurement_times))

            data.append([well_id, group, replicate, *growth_measurements])
    
    columns = ['Well', 'Group', 'Replicate'] + [f't{time}' for time in measurement_times]
    return pd.DataFrame(data, columns=columns)

# Simulating the bacterial growth data with the new format
data = simulate_growth_data_pivot()
data = data.drop(columns=['Group', 'Replicate'])
data.to_csv('OD.csv', index = False)
#print(data)



