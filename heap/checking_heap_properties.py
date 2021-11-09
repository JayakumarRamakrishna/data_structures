#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 18:13:23 2021

@author: jramakrishna
"""

# Problem statement - check whether a list contains a valid min heap or not.
# Example - Check 2i + 2 <= N
# Solution - check the heap properties (in a min heap the parent is smaller than the children)

def is_min_heap(heap):
     # No need to check leaf nodes
     num_items = (len(heap)  - 2) // 2
     
     for i in range(num_items):
         
         # Check Heap property - parent must be smaller than child
         if heap[i] > heap[2*i+1] or heap[i] > heap[2*i+2]:
             return False
     
     return True
 
    
     
     
if __name__ == '__main__':
    n =[4,1, 2, 5, 6]
    print(is_min_heap(n))