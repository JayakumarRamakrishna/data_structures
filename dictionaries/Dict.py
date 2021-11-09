#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:50:39 2021

@author: jramakrishna
"""


class HashTable:
    
    def __init__(self):
        # Size of DS can be changed based on load factor - Dynamic resizing
        self.capacity = 10
        self.keys = [None] * self.capacity
        self.value = [None] * self.capacity
    
    # Calc hash value(index) based on the key
    def hash_function(self, key):
        hash_sum = 0
        
        for letter in key:
            hash_sum = hash_sum + ord(letter)
            
        return hash_sum % self.capacity
    
    def insert(self, key, data):
        
        # Find the valid location for value
        index = self.hash_function(key)
        
        # there may collisions - index is occupied
        # when array is not empty
        while self.keys[index] is not None:
            # update value when same key is present
            if self.keys[index] == key:
                self.value[index] = data
                return
            
            # Linear probing - try next slot
            index = (index + 1) % self.capacity
        
        
        # found valid valid slot  
        self.keys[index] = key
        self.value[index] = data
        
        
    def get(self, key):
        
        # Find the valid location for value
        index = self.hash_function(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.value[index]
            
            # Linear probing - try next slot
            index = (index + 1) % self.capacity
            
        return None
        
        
                
    
    
if __name__ == '__main__':
    
    table = HashTable()
    table.insert('Adam', 23)
    table.insert('Kevin', 45)
    table.insert('Daniel', 34)
    table.insert('Daniel', 33)
    
    print(table.get('Daniel'))
    
     
        
        
        
        
        