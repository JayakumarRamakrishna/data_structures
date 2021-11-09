# -*- coding: utf-8 -*-
"""
Data structre - Arrays
"""

print("hello world")

array = [10, 3, 7, 5]

print(array)

# Random indexing: index starts with 0
# Get nth item in the array
print(array[0]) 

# Get all items in the array
print(array[:]) 

# Get first 2 items in the array
print(array[0:2]) 

# Get all the items in the array except last
print(array[:-1]) 

# Get all the items in the array except last two
print(array[:-2]) 

# Can store mutliple data types in an array
array1 = [10.0, 3, 'jay', 5]
print(array1) 


# Can update an item in an array
array1[2]='kumar'
print(array1) 
########### Above operations have O(1) constant time complexity ###########

###########  Finding max item in an array  is a linear search operation uses O(N) Linear time complexity ###########

array2 = [10, 42, 55, 2, 1, 0]

max = array2[0]

for item in array2:
    if item > max:
        max = item
    
print(max)
        
        