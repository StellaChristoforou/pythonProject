import numpy as np

arr=np.array([10,20,30,40,50])
arr1 = np.array(10)
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr3 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr1.ndim, arr2.ndim, arr3.ndim)
print(arr2[0])
print(arr3[1,1])
print(arr3[0,-1])
print(arr[1:4])
print(arr[2:])
print(arr[:4])
print(arr2[0:7:2])
print(arr3[1,0:2])
print(arr3.shape)

arr4 = np.array([1, 2, 3, 4, 5])
copy = arr4.copy()

copy[0] = 24

print(arr4)
print(copy)

arr5 = np.array([1, 2, 3, 4, 5])
view = arr5.view()

view[0] = 24

print(arr5)
print(view)

arr6=np.array([1,2,3,4,5,6])
print(arr6.reshape(2,3))
print(arr6)

arr7=np.array([1,2,3,4,5,6])
arrList=np.array_split(arr7,3)

for arr in arrList:
    print(arr)

print(np.where(arr7%2==0))

arr8=np.array([1,2,3,2,3,2,7])
print(np.where(arr8==2))

arr9=np.array([2,3,1,5,6,4,7])
print(np.sort(arr9))

arr10=np.array([1,2,3,4])
arr11=np.array([5,6,7,8])

print(np.add(arr10,arr11))
print(np.subtract(arr10,arr11))
print(np.multiply(arr10,arr11))
print(np.divide(arr10,arr11))
print(np.power(arr10,arr11))
print(np.mod(arr10,arr11))
print(np.absolute(arr11))

arr12=np.array([1.23,3.45,6.78])
print(np.trunc(arr12))
print(np.fix(arr12))
print(np.around(arr12,1))
print(np.floor(arr12))
print(np.ceil(arr12))

arr13=np.array([1,2,3,4])
print(np.log(arr13))
print(np.log2(arr13))
print(np.log10(arr13))

arr14=np.array([1,2,3,4])
arr15=np.array([5,6,7,8])
print(np.sum([arr14,arr15]))
print(np.sum([arr14,arr15],axis=1))
print(np.prod([arr14,arr15]))
print(np.prod([arr14,arr15],axis=1))

arr16=np.array([1,2,3])
print(np.cumsum(arr16))
print(np.cumprod(arr16))

arr17=np.array([1,2,3,4,5])
print(np.lcm.reduce(arr17))
print(np.gcd.reduce(arr17))

arr18=np.array([np.pi/2,np.pi/3,np.pi/4])
print(np.around(np.sin(arr18),8))
print(np.around(np.cos(arr18),8))
print(np.around(np.tan(arr18),8))

arr19=np.array([90,180,360])
arr19=np.deg2rad(arr19)
print(arr19)
arr19=np.rad2deg(arr19)
print(arr19)

print(np.hypot(3,4))