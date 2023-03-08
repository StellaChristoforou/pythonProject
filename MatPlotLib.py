import matplotlib.pyplot as plt
import numpy as np

'''
plt.plot([0,10],[0,300])
plt.show()

plt.plot([0,10],[0,300],'o')
plt.show()

plt.plot([0,2,4,6,8,10],[3,1,8,10,5,12])
plt.show()

plt.plot([0,2,4],[3,8,1],marker='o')
plt.show()

plt.plot([0,2,4],[3,8,1],ls='dotted')
plt.show()

plt.plot([0,10],[0,300])
plt.title("Title")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()
plt.show()

plt.subplot(2,1,1)
plt.plot([0,2,4,6,8,10],[3,8,1,10,5,12])
plt.subplot(2,1,2)
plt.plot([0,10],[0,300])
plt.show()

x=np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
y=np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
plt.scatter(x,y)
plt.show()

x = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
y = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
plt.scatter(x, y)
x = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
y = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
plt.scatter(x, y)
plt.show()

x=np.array(["A","B","C","D"])
y=np.array([4,5,6,7])
plt.bar(x,y)
plt.show()

x=np.array(["Potatoes","Bacon","Tomatoes","Sausages"])
y=np.array([25,35,15,25])
plt.pie(y,labels=x)
plt.legend()
plt.show()
'''