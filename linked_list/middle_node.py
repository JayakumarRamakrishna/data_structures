#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:41:08 2021

@author: jramakrishna
"""


##### Find a middle node in a Linked List ##########
# problem statement - Find a middle node in a Linked List without the need of extra memory
# Examples - [10,20,30,40,50] - middle number is 30

# O(N) linear running time complexity

# Solution -  Use 2 pointers, First pointer to travese the linked list one node at a time. Second pointer to traverse the linked list two nodes at a time.
# When faster pointer reaches the end of the list then slower pointer reaches middle node.

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next_node = None
    
 
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.numOfNodes = 0
        
    # O(N) linear running time complexity
    def get_middle_node(self):
        
        fast_pointer = self.head
        slow_pointer = self.head
        
        while fast_pointer.next_node is not None and fast_pointer.next_node.next_node is not None:
            
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node
        
        return slow_pointer.data
        
        

        
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
        
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node
            
            
if __name__ == '__main__':
    
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.insert(40)
     

    print(linked_list.get_middle_node())
  
    
    
        

        actual_node = self.head