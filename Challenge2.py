import matplotlib.pyplot as plt #Step1
import numpy as np

data=pd.read_csv("1.supermarket.csv") #Step2

q=data.groupby("item_name").quantity.sum() #Step3


plt.bar(q.index,q,color=['orange','purple','yellow','red','green','blue','cyan']) #Step4
plt.xlabel('Items')
plt.xticks(rotation=6)
plt.ylabel('Number of Items Ordered')
plt.title("Most Ordered Supermarket\'s Items")

plt.show()




