# Creating 1-D , 2-D & 3-D Arrays using Numpy

import numpy as np

arr1d = np.array([1,2,3,4,5])
print(arr1d)
print(arr1d.ndim) #### it(ndim) is used for determing the dimension of the array.... 
print(arr1d.shape)
print("___________________________________")


arr2d = np.array([[1,2,3,4],[9,8,7,6]])
print(arr2d)
print(arr2d.ndim)
print(arr2d.shape)
print("___________________________________")


arr3d = np.array([[[1,2,3,4,6],[6,4,6,8,2]],[[82,4,5,6,3],[1,4,5,6,3]]])
print(arr3d)
print(arr3d.ndim)
print(arr3d.shape)
print("___________________________________")
