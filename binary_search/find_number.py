#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 12:13:34 2021

@author: jramakrishna
"""
# Problem statement - find a number is a sorted array
# Examples -   [1,2,3,4,5] find 3
# Solution : use binary search method - O(logN) linear running time complexity

def search(nums, data):
    start_length = 0
    end_length = len(nums) - 1
    
    while start_length <= end_length:

        
        middle_length = (start_length + end_length)//2
        
        if data == nums[middle_length]:
            return data
        elif data < nums[middle_length]:
            end_length = middle_length - 1
        else:
            start_length = middle_length + 1
    return -1

            

if __name__ == '__main__':
    
    
    n = [ 1, 2, 3, 4, 5, 6, 7, 8]
    print(search(n, 6))