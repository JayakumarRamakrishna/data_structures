#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 20:49:17 2021

@author: jramakrishna
"""


class Node:
    
    def __init__(self, data, parent):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.height = 0
        
        
class AVLTrees:
    
     
    def __init__(self):
        #we can access root seperately
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)
            
    def insert_node(self, data, node):
        
        # Consider left subtree
        if data < node.data:
            # IF Left child is not None
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node (data, node)
                node.height = max(self.calc_hieght(node.left_child), self.calc_hieght(node.right_child)) + 1
                
        else:
             # IF Right child is not None
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node (data, node)
                node.height = max(self.calc_hieght(node.left_child), self.calc_hieght(node.right_child)) + 1
               
                
        # After every insertion we have check AVL properties are violated
        self.handle_violation(node)
        
        
            
    
    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)
    
    def remove_node(self, data, node):
        
        if node is None:
            return
    
        if data < node.data:
            self.remove_node(data, node.left_child)
        elif data > node.data:
            self.remove_node(data, node.right_child)
        else:
            # found node to remove
            #case 1 - Node is leaf Node
            
            
            
        
            
            
                
            
            
            
            
        