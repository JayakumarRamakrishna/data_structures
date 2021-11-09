#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:16:03 2021

@author: jramakrishna
"""


class Node:
    
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        
        
def dfs_with_recursion(start_node):
    
    start_node.visited = True
    
    print(start_node.name)
    
    for n in start_node.adjacency_list:
        if not n.visited:
            dfs_with_recursion(n)
            
if __name__ == '__main__':
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')
    
    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node2.adjacency_list.append(node5)
    
    dfs_with_recursion(node1)
    
    
    
            
    