#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 23:52:33 2021

@author: jramakrishna
"""


def firstUniqChar(s):
    frequency = {}
    for i in s:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] +=1
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i
    return -1

print(firstUniqChar("people"))
print(firstUniqChar("abaabba"))