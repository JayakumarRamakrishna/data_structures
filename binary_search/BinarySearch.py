#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:29:56 2021

@author: jramakrishna
"""

class Node:
    
    def __init__(self, data, parent):
        self.data = data
        self.left_child= None
        self.right_child = None
        self.parent = parent
        
    
    
class BinarySearchTree:
    
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
            
    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)
        
    def get_max(self, node):
        
        if node.right_child:
            return self.get_max(node.right_child)
        
        return node.data    
        
    
    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)
        
    def get_min(self, node):
        
        if node.left_child:
            return self.get_min(node.left_child)
        
        return node.data    
      


            
                
bst = BinarySearchTree()
bst.insert(30)       
bst.insert(10)  
bst.insert(20)   
bst.insert(50)  
bst.insert(40)
bst.insert(410)
bst.insert(-5)


bst.traverse() 

print('max item %d' %bst.get_max_value())

print('min item %d' %bst.get_min(bst.root))
              
           
        
        
            
            
            
        
        
    