import pandas as pd
import numpy as np

'''
x=[23,48,19]
myfirstseries=pd.Series(x)
print(myfirstseries)
print()

data={"students":["Emma","John","Bob"],"grades":[12,18,17]}
myfirstdataframe=pd.DataFrame(data)

print(myfirstdataframe)
print()

print(myfirstdataframe["students"])
print()

myfirstdataframe=pd.DataFrame(data,index=["a","b","c"])
secondrow=myfirstdataframe.iloc[1]
print(secondrow)
print()
'''

'''
data = {"students": ['Emma', 'John', 'Mary', 'Bob'],"grades": [12, np.nan, 18, np.nan]}
my_first_df=  pd.DataFrame(data, index=["a", "b", "c","d"])
#print(my_first_df.isnull())
'''

'''
my_first_df["students"].fillna("No Name",inplace=True)
my_first_df["grades"].fillna("No Grade",inplace=True)
#print(my_first_df)


df2=my_first_df.replace(to_replace="Bob",value="Alice")
print(df2)


df=my_first_df.interpolate(method="linear",limit_direction="forward")
print(df)

my_first_df.dropna(inplace=True)
print(my_first_df)
'''

'''
s=pd.Series(["Workearly","e-learning","Python"])
for index,value in s.items():
    print(f"index: {index}, Value: {value}")
'''
data={"students":["Emma","John"],"grades":[12,19.8]}
mydf=pd.DataFrame(data,index=["a","b"])

'''
for i,j in mydf.iterrows():
    print(i,j)
    print()
'''

column=list(mydf)
for i in column:
    print(mydf[i][1])