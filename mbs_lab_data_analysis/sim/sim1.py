
import numpy as np
import pandas as pd










# top table
well_A = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15']
OD = [i + np.random.normal(0.5, 2, len(well_A)) for i in range(10, 6*16+10)]

df = pd.DataFrame()
df['well_A'] = well_A
for i, time in enumerate(range(len(OD))):
    name = 'OD'+str(time)
    df[name] = OD[i]


df.to_csv('OD.csv', index=False)



























