#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 19:54:16 2021

@author: jramakrishna
"""


# Problem statement - Write an efficient algorithm thats able to compare two binary search trees.
# Example - The method returns true if the trees are identical (same topology with same values in the nodes) otherwise it returns false.
# Solution - Use In order traversal

class TreeComparator(object):
    
    def compare_trees(self, node1, node2):
        
        if not node1 or not node2:
            return node1 == node2
        
        if node1.data is not node2.data:
            return False
        
        return self.compare_trees(node1.left_child, node2.left_child) and self.compare_trees(node1.right_child, node2.right_child)
    

class Node(object):
    
    def __init__(self, data, parent):
        self.data = data
        self.left_child= None
        self.right_child = None
        self.parent = parent
        
    
    
class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)
            
    def insert_node(self, data, node):
        
        # go the Left subtree
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
                
          # go the right subtree       
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)
                
    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)
            
            
    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)
            
        print('%s' % node.data)
        
        if node.right_child:
            self.traverse_in_order(node.right_child)    
            
            
if __name__ == '__main__':
    
    bst = BinarySearchTree()
    bst.insert(30)       
    bst.insert(10)  
    bst.insert(20)   
    bst.insert(50)       
        
    bst2 = BinarySearchTree()
    bst2.insert(30)       
    bst2.insert(10)  
    bst2.insert(20)   
    bst2.insert(50)  
    
    comparator = TreeComparator()
    print(comparator.compare_trees(bst.root, bst2.root)) 
