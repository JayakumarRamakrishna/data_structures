#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 19:40:20 2021

@author: jramakrishna
"""


#### Reversing an array in-place  ######
# Problem statement - Reverse a T[] array in O(N) linear time complexity and we want the algorithm to be in-place as well - so no additional memory can be used!

# Example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

# Solution: Replace first item with nth, then 2nd item with (n-1)th until we get middle value


def reverse(nums):
    # index pointing to the first index
    start_index = 0
    
    # index pointing to the last index
    end_index = len(nums) -1 
    
    while end_index > start_index:
        # Keep swaping the items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
        

if __name__ == '__main__':
    
    nums = [1,2,3,4,5,6]
    reverse(nums)
    print(nums)
    
    
        
        
    
    