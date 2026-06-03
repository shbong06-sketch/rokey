# pd_DataFrame.py

import pandas as pd

data = [
    [1, 'Alice', 30],
    [2, 'Bob', 35],
    [3, 'Charlie', 25]
]

df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])
print(df)
print(type(df))

print("------------------")
data = {
    'ID' : [1, 2, 3],
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [30, 35, 25]
}

df = pd.DataFrame(data)
print(df)
