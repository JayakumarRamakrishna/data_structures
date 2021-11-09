#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 23:29:49 2021

@author: jramakrishna
"""

########### Duplicates in an array  ############

# Problem statement - find duplicates in a one-dimensional array of integers in O(N) running time where the integer values are smaller than the length of the array!

# Examples - list [1, 2, 3, 1, 5] then the algorithm can detect that there are a duplicate with value 1.

# O(N) linear running time complexity

# Solution :
# 1. Brute-force approach (comparing items with all the rest) - has O(N2) running time
# 2. Hash maps - Travese the given array & try insert each item in a hashtable with the value as key. If you can't insert then the item is duplicate
# 3. Using absolute values - O can achieve (N) linear running time complexity


def find_duplicates(nums):
    
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = - nums[abs(num)] 
            print(nums)
            
        else:
            print('duplicates found : %s' % str(abs(num)))
            

def search(nums, data):
    start_length = 0
    end_length = len(nums) - 1
    
    while start_length <= end_length:
        print(start_length, end_length)
        
        middle_length = (start_length + end_length)//2
        print(middle_length)
        
        if data == nums[middle_length]:
            return data
        elif data < nums[middle_length]:
            end_length = middle_length - 1
        else:
            start_length = middle_length + 1
    return -1

            

if __name__ == '__main__':
    
    # this method cannot handle values < 0
    # Maximum  item is smaller than the length of the array!
    n = [ 2, 6, 5, 1, 4, 3, 2, 4]
    find_duplicates(n)
    
    n = [ 1, 2, 3, 4, 5, 6, 7, 8]
    print(search(n, 1))
            
            