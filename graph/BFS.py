#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 10:53:42 2021

@author: jramakrishna
"""




class Node:
    
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        
        
def breadth_first_search(start_node):
        
        # FIFO
        queue = [start_node]
        
        # keep iterating(considering neighbours) until the queue become empty
        while queue:
            
            # Remove and return first item in the list
            actual_node = queue.pop(0)
            actual_node.visited = True
            
            print(actual_node.name)
            
            # Let's consider the neighbours of the actual node one by one
            for n in actual_node.adjacency_list:
                if not n.visited:
                    queue.append(n)
            
            
    
    


if __name__ == '__main__':
    
    # Create nodes or vertices
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    
     # handle the neighbours
    
    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)
    
    # Run BFS algorithm
    breadth_first_search(node1)
    
    
    
    