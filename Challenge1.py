import pandas as pd #Step1
import numpy as np

data=pd.read_csv("1.supermarket.csv") #Step2
'''
print(data.head()) #Step3
print("Shape of Data:",data.shape)
print(data.info())
'''

print(data.columns)

x=data.groupby("item_name")
x=x.sum()
print(x.head(1))