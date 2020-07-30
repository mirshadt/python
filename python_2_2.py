# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 21:17:35 2020

@author: Irshad
"""

name = input('input a string:')

for i in range(len(name),0,-1):
    print(name[i-1],end="")