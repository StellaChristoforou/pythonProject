import pandas as pd
import numpy as np

df=pd.read_csv("finance_liquor_sales.csv")
'''
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
mean=df.mean(numeric_only=True)
print(mean)
median=df.median(numeric_only=True)
print(median)
max_v=df.max(numeric_only=True)
print(max_v)
summary=df.describe()
print(summary)
cn=df.grouby("category_name")
print(cn.first())
cnc=df.groupby(["category_name","city"])
print(cnc.first())
cn=df.groupby("category_name")
print(cn.aggregate(np.sum))
cnc = df.groupby(['category_name', 'city'])
print(cnc.agg({'bottles_sold': 'sum', 'sale_dollars': 'mean'}))
cnc=df.groupby("vendor_name")
print(cnc.filter(lambda x: len(x)>=20))
'''
