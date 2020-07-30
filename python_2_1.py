# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:25:51 2020

@author: Irshad
"""

for i in range(0,5):
    for j in range (0,i+1):
        print('*',end="")
    print()
for i in range(5,0,-1):
    for j in range (0,i):
        print('*',end="")
    print()