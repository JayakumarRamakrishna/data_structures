#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 09:18:06 2021

@author: jramakrishna
"""


def splitArr(num):
    one = []
    two = []
    length = len(num)
    for i in range(0,length):
        if (num[i] in one ) and (num[i] in two):
            return print("NA")
        elif (num[i] in one) and not (num[i] in two):
            two.append(num[i])
        elif not (num[i] in one) and (num[i] in two):
            one.append(num[i])
        elif (i%2) == 0:
            two.append(num[i])
        else:
            one.append(num[i])
    return print(one , two)
    

if __name__ == '__main__':
    num = [1, 2, 2, 3, 4, 3, 5, 6]
    splitArr(num)
