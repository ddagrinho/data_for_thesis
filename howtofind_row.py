import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
from scipy.interpolate import splrep, splev



# Create a sample DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                   'Age': [25, 30, 35, 40],
                   'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']})

# Find the position of 'Charlie' in the DataFrame
value = 'Charlie'  # Value to search for

# Get the row label
row_label = df.index[df['Name'] == value].tolist()[0]

# Get the column label
column_label = 'Name'

# Get the row and column indices
row_index = df.index.get_loc(row_label)
column_index = df.columns.get_loc(column_label)

# Print the results
print(f"Value '{value}' is located at row '{row_label}', column '{column_label}', "
      f"row index {row_index}, column index {column_index}.")

