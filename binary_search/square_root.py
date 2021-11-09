#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 08:01:33 2021

@author: jramakrishna
"""


# Problem statement - find square root of the number
# Examples -   square root of 4  is 2  10 ---> 3.16
# Solution : use binary search method - O(lonN) linear running time complexity



def square(num, i, j):
    mid = (i + j) / 2
    sq = mid * mid
    print('mid',mid)
    print('sq', sq)
    
    if ((sq == num ) or (abs (sq - num) < 0.0001)):
        return mid
    elif sq < num:
        return square(num,mid,j)
    else:
        return square(num,i, mid)
    
def squre_root(num):
    i = 1
    found = False
        
    while found == False :
        if i*i  == num:
            print(i)
            found = True
                
        elif i * i > num:
            root = square(num,i-1, i)
            print('square root num is %0.2f' %root)
            found = True
        i += 1
            
    
        

if __name__ == '__main__':
    squre_root(4)
        
    
             
    
                  

                  
            
            
            
            
            
        
        
    
    