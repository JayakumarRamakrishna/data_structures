#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:37:14 2021

@author: jramakrishna
"""


class SelectionSort:
    
    def __init__(self, nums):
        self.nums = nums
    
    
    def sort(self):
        
        # (N-1) * O(N) = O(n2) quadratic time complexity
        for i in range(len(self.nums)-1):
            
            # stores index of min item
            index = i
            
            # Linear time complexity O(N)
            for j in range(i, len(self.nums)):
                if self.nums[j] < self.nums[index]:
                    index = j
                
            # swap min item with leftmost item
            if index !=i:
                self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
                

if __name__ == '__main__':
     n = [5, 4, 3, 2, 1]
     
     selection_sort = SelectionSort(n)
     selection_sort.sort()
     print(selection_sort.nums)
     
     
     
                    