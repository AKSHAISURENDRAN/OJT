import numpy as np
array_2D = np.array(
    [
    [1,2,3],#0
    [4,5,6]#1
     ]
    )

#accessing a single element 
element = array_2D[0,1]
print("element at the index of [1,2]", element)

#Access by 2row
row = array_2D[1:]
print("second row:",row)


#Access by 1row
row = array_2D[0:]
print("first row:",row)

#Access by column
column = array_2D[:,1]
print ("second column :",column)

#Slicing
#access the sub array with row of 0 and 1, column of  1 and 2
slice_array = array_2D[0:2,1:3]
print("subarray:",slice_array)