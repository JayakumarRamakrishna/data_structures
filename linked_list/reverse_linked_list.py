#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 19:16:01 2021

@author: jramakrishna
"""
######## Reverse a linked list #########
# Problem statement - construct a inplace algorithm to reverse a linked list 
# Example - [1, 2, 3, 4] ---> [4, 3, 2, 1] 
# O(N) linear running time complexity

# Solution -  use pointers to achive inplace algorithm

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next_node = None
    
 
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.numOfNodes = 0
        
    # O(N) linear running time complexity
    def reverse(self):
        
        current_node = self.head
        previous_node = None
        next_node = None
        
        while current_node is not None:
            
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
            
        
        self.head = previous_node
        
        
    def insert(self, data):
        
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            
        else:
            new_node.next_node = self.head
            self.head = new_node
            
            
 
        # O(N) Linear running time complexity
    def traverse(self):
        
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node
            
            
if __name__ == '__main__':
    
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.insert(40)

linked_list.traverse()
linked_list.reverse()
print ("--------------")
linked_list.traverse()

    
    