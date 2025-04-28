import numpy as np

# One dimensional array
arr=np.array([1,2,3,4])
# print (arr)

# two dimensional array
arr2=np.array([[1,2,3,4],[5,6,7,8]])
# print (arr2)

# with default as zero one dimensional here (3) is number of zeros in the row (shape)

arrz=np.zeros(3)
# print (arrz)

#with two dimensional zeroes here (3) is number of rows and (4) is number of columns
arrz2=np.zeros((3,4))  #(3,4) is called as shape 
# print (arrz2)

# if we want the defailt values to be ones

arrones=np.ones((2,3))
# print(arrones)

# if we want default value not zero or one we can use full function
arrfull=np.full((2,3),5) #(2,3) is shape and 5 is the default value we want
# print(arrfull)

# creating sequences of numbers in numpy
#using arange() function
#arange(start,stop,step) start is the starting value,stop is the last value it will be excluded and run upto -1 and step is number by which we need to step up or say skip
arrarange=np.arange(1,11,2)
# print(arrarange)

# crating Identity matrix using numpy
#we will use eye() function eye(size)
Identity_matrix=np.eye(5)
print(Identity_matrix)