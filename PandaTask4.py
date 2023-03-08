import pandas as pd

data=pd.read_csv("data.csv")
for i,j in data.iterrows():
    print(i,j)
    print()
