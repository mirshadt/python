# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 19:29:07 2020

@author: Irshad
"""
numbers = []
for i in range(2000,3201):
    if(i%7==0 and i%5!=0):
        numbers.append(i)
print(*numbers,sep=', ')