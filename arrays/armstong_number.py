#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 21:12:04 2021

@author: jramakrishna
"""
# problem statement - Find Armstrong number from given list of numbers
# Examples -  153 =  pow(1,3) + pow(5,3) + pow(3,3)
# O(N) linear running time complexity

    
def is_armstrong_num(arr):
    temp = 0
    input_num = arr[0]
    for i in range(1, input_num+1):
        sum = 0
        temp = arr[i]
        while i > 0 and temp > 0:
            digit = temp % 10
            sum += pow(digit,3)
            temp //= 10
            
        if arr[i] == sum:
            print(arr[i], ' is an armstrong num')
        else:
            print(arr[i], ' is not an armstrong num')
            
            
if __name__  == '__main__':
    
    arr = [5, 153, 123, 370, 180, 407]
    is_armstrong_num(arr)
    
            
    