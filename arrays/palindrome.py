#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 20:05:21 2021

@author: jramakrishna
"""

########### Palindrome  ############

# Problem statement - Palindrome is a string that reads the same forward and backward

# Examples - Palindrome

# O(N) linear running time complexity

# Solution -  Replace first item with nth, then 2nd item with (n-1)th until we get middle value and then compare old and reversed string

def palindrome(s):
    if s == s[::-1]:
        return True
    
    return False




def is_palindrome(str):
    
    original_string = str

    reverse_string = reverse(str)

    if original_string == reverse_string:
        return True
    
    return False
    
        
def reverse(str):
    #Convertstring to list of characters
    data = list(str)
    
    # index pointing to the first index
    start_index = 0
    
      # index pointing to the last index
    end_index = len(data) - 1
    
    while end_index > start_index:
        # kepp swappin the items values
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
        
    # Transform list of letters to string 
    return ''.join(data)

if __name__ == '__main__':
    print(is_palindrome('madam'))
    
    
