#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 14:51:05 2021

@author: jramakrishna
"""

class Node:
    
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        
        
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Inserts items at the end of DLL.
    # So we need to manipulate the tail node in O(1) constant time complexity
    def insert_end(self, data):
       new_node = Node(data)
       # when list is empty
       if self.head is None:
           self.head = new_node
           self.tail = new_node
           # when list has atleast one item
       else:
           new_node.previous = self.tail
           self.tail.next = new_node
           self.tail = new_node
       
    
    # We can traverse a Doubly Linked List in both direction
    def traverse_forward(self):
        
        actual_node = self.head
        
        while actual_node is not None:
            print('%d' % actual_node.data)
            actual_node = actual_node.next
    
        
    def traverse_backward(self):
        
        actual_node = self.tail
        
        while actual_node is not None:
            print('%d' % actual_node.data)
            actual_node = actual_node.previous
            
            
if __name__ == '__main__':
    
    linked_list = DoublyLinkedList()
    linked_list.insert_end(1)
    linked_list.insert_end(2)
    linked_list.insert_end(3)
    linked_list.insert_end(4)
    
    linked_list.traverse_forward()
    print ("--------------")
    linked_list.traverse_backward()
    