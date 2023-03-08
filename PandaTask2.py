import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11],'col2': [4, 5, 6, 9, 5, 0],'col3': [7, 5, 8, 12, 1,11]}
df=pd.DataFrame(d)
s1=df.iloc[:,0]
print("The first column as a Series")
print(s1)
print(type(s1))