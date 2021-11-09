#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:19:20 2021

@author: jramakrishna
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:37:14 2021

@author: jramakrishna
"""


class InsertionSort:
    
    def __init__(self, nums):
        self.nums = nums
    
    
    def sort(self):
        
        # (N-1) * O(N) = O(n2) quadratic time complexity
        for i in range(len(self.nums)):
            
            j = i
            # check all previous items
            while j > 0 and self.nums[j-1] > self.nums[j]:
                
                # swap items - N * N time complexity
                self.nums[j-1], self.nums[j] = self.nums[j], self.nums[j-1]
                j = j-1

                

if __name__ == '__main__':
     n = [1, -5, 10, 100, 4, 0, 3, 2, 1]
     
     insertion_sort = InsertionSort(n)
     insertion_sort.sort()
     print(insertion_sort.nums)
     
     
     
                    