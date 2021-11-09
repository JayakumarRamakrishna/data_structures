#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 21:55:53 2021

@author: jramakrishna
"""

########### Anagram  ############

# Problem statement - An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once

# Examples - restful and fluster

#  O(NlogN) linearithmic running time complexity

# Solution -  Sort the letters of each string and compare the letters at the same index


def is_anagram(str1, str2):
    
    # if the len of str1 and str2 are not equal then they are not anagrams
    if len(str1) != len(str2):
        return False
    
    # Sort the letters of each string and compare the letters at the same index
    # This is bottleneck beacuse of O(NlogN) linearithmic running time complexity
    str1 = sorted(str1)
    str2 = sorted(str2)
    print(str1)
    
    print(str2)
    # compare the letters at the same index 
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
        
    return True

# Overall running time is O(NlogN) + O(N) = O(NlogN)
if __name__ == '__main__':
    s1 = ['r', 'e', 's', 't', 'f', 'u','l']
    s2 = ['f', 'l', 'u', 's', 't', 'e', 'r']
    print(is_anagram(s1, s2))
