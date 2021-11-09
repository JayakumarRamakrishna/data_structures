#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 15:34:05 2021

@author: jramakrishna
"""

# Max in a stack problem overview
# Problem statement - Find the maximum item of a stack in O(1) running time complexity. We can use O(N) extra memory!
# Solution - We can use another stack to track the max item!

class MaxStack:
    
    def __init__(self):
        # use main stack to insert
        self.max_stack = []
        self.main_stack = []
        
        # Adding an item to the queue. O(1) constant time complexity
    def push(self, data):
        # push new item to main stack
        self.main_stack.append(data)
        
        # First item is same for both main & max stack
        
        if(len(self.main_stack) == 1):
            self.max_stack.append(data)
            return
            
        # push only max item among data & last item on max stack
        if (data > self.max_stack[-1]):
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])
        
        
        
    def peek(self):
        return self.main_stack[-1]
     
    def get_max(self):
        return self.max_stack[-1]
    
    
if __name__ == '__main__':
    
    stack = MaxStack()
    stack.push(1000)
    stack.push(20)
    stack.push(200)
    stack.push(300)
    stack.push(50)
    print('last item:  %d' %stack.peek())
    print('Max item:  %d' %stack.get_max())
        

