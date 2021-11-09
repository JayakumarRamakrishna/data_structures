#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:22:29 2021

@author: jramakrishna
"""


class BubbleSort:
    
    def __init__(self, nums):
        self.nums = nums
    
     # takes in O(N2) running time complexity
    def sort(self):
        
        for i in range(len(self.nums) -1):
            for j in range(len(self.nums)-i-1):
                if self.nums[j] > self.nums[j+1]:
                    self.swap(j,j+1)
                    
        
    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        
        
if __name__ =='__main__':
    
    n = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    
    bubble_sort = BubbleSort(n)
    bubble_sort.sort()
    print(bubble_sort.nums)
    
    
        
        