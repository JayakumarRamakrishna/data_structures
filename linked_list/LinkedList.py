# -*- coding: utf-8 -*-
"""
Data structre - Linked List
"""
import time

class Node:
    
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.numOfNodes = 0
        
    # O(1) constant running time complexity
    def insert_start(self, data):
        
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            
        else:
            new_node.nextNode = self.head
            self.head = new_node
        
     # O(N) Linear running time complexity
    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        
        actual_node = self.head
        
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode
            
        actual_node.nextNode = new_node
        
     # O(N) Linear running time complexity   
    def remove(self, data):
        
        if self.head is None:
            return
        
        actual_node = self.head
        previous_node = None
        
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode
            
        
        #search miss - Item not present in the linked list
        if actual_node is None:
            return 
        
        self.numOfNodes = self.numOfNodes - 1
        
        if previous_node is None:
            self.head = actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode
            
            
        
            
        
        

    
    # O(1) constant running time complexity    
    def size_of_linkedlist(self):
        return self.numOfNodes
    
    # O(N) Linear running time complexity
    def traverse(self):
        
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode
            
            
linked_list = LinkedList()
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(7)
linked_list.insert_end(10)
linked_list.insert_end(100)
linked_list.insert_end(1000)

linked_list.traverse()
print('size : %d' %linked_list.size_of_linkedlist())
linked_list.remove(1000)
print('size : %d' %linked_list.size_of_linkedlist())
print ("--------------")
linked_list.traverse()





if __name__ == '__main__':
    
    linked_list = LinkedList()
    
    now = time.time()
    
    for i in range(500000):
        linked_list.insert_start(i)
        
    print('Insterting itmes into Linked List in %ss' % str(time.time() - now))
        
    array = []
    
    now = time.time()
    
    for i in range(500000):
        array.insert(0, i)
        
    print('Insterting   itmes into Array in %ss' % str(time.time() - now))
    
    
    
    
    
    




