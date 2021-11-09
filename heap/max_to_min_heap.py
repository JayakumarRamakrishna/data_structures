#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 18:35:42 2021

@author: jramakrishna
"""

# Problem statement - check whether a list contains a valid min heap or not.
# Example - Check 2i + 2 <= N
# Solution - Nonned check the heap properties. Consider internal nodes in a reverse order + call fixDown  method

class HeapTransformer:
    
    def __init__(self, heap):
        self.heap = heap
 
    
    def transform(self):
        
        for i in range((len(self.heap)-2)//2, -1, -1):
            self.fix_down(i)
            
    def fix_down(self, index):
        
        index_left = 2 * index + 1
        index_right = 2 * index + 2
        
        # in max heap, parent > child
        index_largest = index
        
        # get min of parent or left child
        if index_left < len(self.heap) and self.heap[index_left] < self.heap[index]:
            index_largest = index_left
            
         # get min of parent or right child
        if index_right < len(self.heap) and self.heap[index_right] < self.heap[index_largest]:
            index_largest = index_right
            
        if index != index_largest:
            self.heap[index], self.heap[index_largest] = self.heap[index_largest], self.heap[index]
            self.fix_down(index_largest)
            
        
        
        
        
if __name__ == '__main__':
    
    n = [210, 100, 23, 5, 2]
    
    heap_transform = HeapTransformer(n)
    heap_transform.transform()
    print(heap_transform.heap)
    
        