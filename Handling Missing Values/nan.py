'''
Finding Nan values
'''
import numpy as np
arr=np.array([1,2,np.nan,5,6,np.nan,33])

print(np.isnan(arr))

'''
Nan to num
np.nan_to_num(array,nan=value) default is 0
'''

cleaned_arr=np.nan_to_num(arr,nan=4)
print(cleaned_arr)

'''
Identifying infinity values
use np.isinf()
'''
arrinf=np.array([1,2,np.inf,5,6,-np.inf,33])
print(np.isinf(arrinf))

'''
replacing infinite values 
'''

print(np.nan_to_num(arrinf,posinf=10,neginf=-10))