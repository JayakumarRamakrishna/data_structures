#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:45:03 2021

@author: jramakrishna
"""


class ShellSort:
    
    def __init__(self, nums):
        self.nums = nums
    
    
    def sort(self):
        gap = len(self.nums) // 2
        
        while gap > 0:
            
            for i in range(gap, len(self.nums)):
                
                j = i
                
                while j >= gap and self.nums[j - gap] > self.nums[j]:
                    
                    self.nums[j], self.nums[j - gap] = self.nums[j - gap], self.nums[j]
                    j = j - gap
                    
            gap = gap // 2
                
                
                

                

if __name__ == '__main__':
     n = [10, -4, 0, 3, 2, 1, 100, -8]
     
     shell_sort = ShellSort(n)
     shell_sort.sort()
     print(shell_sort.nums)
     