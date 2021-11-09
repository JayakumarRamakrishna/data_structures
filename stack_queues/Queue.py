#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 12:16:07 2021

@author: jramakrishna
"""

# Queue - FIFO Fast IN First Out

class Queue:
    
    def __init__(self):
        self.queue = []
    
    #O(1) Constant running time complexity    
    def is_empty(self):
        return self.queue == []
    
    #0(1) Constant running time complexity
    def enqueue(self, data):
        self.queue.append(data)
        
    #0(N) Linear running time complexity --- Doubly linked list
    def dequeue(self):
        if self.size() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1
    
    #0(1) Constant running time complexity
    def peek(self):
        data = self.queue[0]
        return data
    
     #0(1) Constant running time complexity
    def size(self):
        return len(self.queue)
    

if __name__ == '__main__':
    
    queue = Queue()
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print("size %d" % queue.size())
    print("dequeue %d" % queue.dequeue())
    print("size %d" % queue.size())
    print("size %d" % queue.size())
    print("dequeue %d" % queue.dequeue())
    print("size %d" % queue.size())
    print("dequeue %d" % queue.dequeue())
    print("size %d" % queue.size())
    print("dequeue %d" % queue.dequeue())
    
    
        
    
    
