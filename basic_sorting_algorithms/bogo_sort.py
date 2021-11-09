#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:00:15 2021

@author: jramakrishna
"""
import random

class BogoSort:
    
    def __init__(self, nums):
        self.nums = nums
        
    
    def sort(self):
        
        while not self.is_sorted():
            print(' Shuffle again...')
            self.shuffle()
    
    # Fisher - Yates approach - generate new permutation in O(N) - inplace
    def shuffle(self):
        for i in range(len(self.nums) -2, -1, -1):
            j = random.randint(0, i+1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            
         
        
    def is_sorted(self):
        
        for i in range(len(self.nums) - 1):
            if self.nums[i] > self.nums[i+1]:
                return False
        
        return True
    

if __name__ == '__main__':
    
    # It has  O(N!) running time complexity
    algorithm = BogoSort([1, -4, 0, 10, 12, -5, 1, 2, -1, 34])
    algorithm.sort()
    print(algorithm.nums)
    