import numpy as np

#create 1-D array
array_1D = np.array([1,2,3,4,5])
print("1d Array:",array_1D)

#create 2D array
array_2D = np.array([[1,2,3],[4,5,6]])
print("2D array:",array_2D)

#create 3D array
array_3D = np.array ([[[1,2,3],[4,5,6],[7,8,9]]])
print("3Darray:",array_3D)

#create an array with ones
array_ones = np.ones((2,4))
print ("Array with ones :",array_ones)

#create an with zeros
array_zeros = np.zeros((3,3))
print("Array with zeros:",array_zeros)

#create an array with a particular range
array_range = np.arange((10))
print ("Array with a range :",array_range)