#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:29:43 2021

@author: jramakrishna
"""


class Node:
    
    def __init__(self, name):
        
        self.name = name
        self.adjacency_list = []
        self.visited = False
        

def depth_first_search(start_node):
    
    # LIFO is used
    stack = [start_node]
    
    while stack:
        actual_node = stack.pop()
        actual_node.visited = True
        print(actual_node.name)
        
        # Let's consider the neighbours of the actual node one by one
        for n in actual_node.adjacency_list:
            if not n.visited:
                stack.append(n)
                
            
            
if __name__ == '__main__':
    
    # Create nodes or vertices
    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node4 = Node("4")
    node5 = Node("5")
    
    # handle the neighbours
    
    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node2.adjacency_list.append(node5)
    
    depth_first_search(node1)
        
        
    
        
        