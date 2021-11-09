#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:33:30 2021

@author: jramakrishna
"""


# stack - LIFO Last IN First Out

class Stack:
    
    def __init__(self):
        self.stack = []
        
        
    #Push - Insert item into Stack - O(1) Constant running time complexity
    def push(self, data):
            self.stack.append(data)
        
    
    #Pop - Remove and return last item in the Stack - O(1) Constant running time complexity
    def pop(self):
        
        if self.stack_size() < 1:
            return -1
        
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    #Peek - Return last item without removing it - O(1) Constant running time complexity
    def peek(self):
        data = self.stack[-1]
        return data
    # O(1) Constant running time complexity
    def is_empty(self):
        return self.stack == []
    
    def stack_size(self):
        return len(self.stack)
    
if __name__ == '__main__':
    
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print('size of stack : %d' %stack.stack_size())

    print('Pop/remove item of stack : %d' %stack.pop())
    print('size of stack : %d' %stack.stack_size())
    print('Peek item of stack : %d' %stack.peek())
    print('size of stack : %d' %stack.stack_size())
    print('Pop/remove item of stack : %d' %stack.pop())
    print('Pop/remove item of stack : %d' %stack.pop())
    print('Pop/remove item of stack : %d' %stack.pop())
        
    



            
    
            