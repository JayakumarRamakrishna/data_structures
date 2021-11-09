#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 23:06:53 2021

@author: jramakrishna
"""

###### reverse a given integer ##########
# Problem statement -  Design an efficient algorithm to reverse a given integer.
# Example - if the input of the algorithm is 1234 then the output should be 4321.

#  O(N) linear running time complexity

def reverse_intiger(n):
    reminder = 0
    reverse_num = 0
    
    while n > 0:
         reminder = n % 10
         n = n//10
         reverse_num = reverse_num * 10 + reminder
    
    
    return reverse_num
         
if __name__ == '__main__':
    
    n =71345
    
    print(reverse_intiger(n))
    
         
