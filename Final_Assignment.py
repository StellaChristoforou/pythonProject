import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("liquor_sales_FinalAssignment1.csv")

'''
x=data.groupby(["zip_code","item_description"]).bottles_sold.max()
print(x)
'''
y=data.groupby('store_name').sale_dollars.sum()
sum_sales=data['sale_dollars'].sum()

percentage=(y/sum_sales)*100


store_names=set(data['store_name'])
s=list(store_names)
sn=np.array(s)
sn_sort=np.sort(sn)

plt.subplot(2,1,1)
plt.pie(percentage,labels=sn_sort)

z=data.groupby('zip_code').bottles_sold.sum()


zc=set(data['zip_code'])
zcs=list(zc)
zip_codes_array=np.array(zcs)
zipcode=np.sort(zip_codes_array)

plt.subplot(2,1,2)
plt.scatter(zipcode, z, color=np.random.rand(len(zipcode),3))
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.show()




