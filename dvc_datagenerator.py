import os
import pandas as pd

data = {'Name' : ['Alice', 'Bob', 'Charlie'],
        'Age'  : [25, 30, 35],
        'City' : ['New York', 'Los Angeles', 'Chicago']
        }

df = pd.DataFrame(data)

new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'city1'}
df.loc[len(df.index)] = pd.Series(new_row_loc)

new_row_loc2 = {'Name': 'GF2', 'Age': 22, 'City': 'city2'}
df.loc[len(df.index)] = pd.Series(new_row_loc2)

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV Saved in the path {file_path}")