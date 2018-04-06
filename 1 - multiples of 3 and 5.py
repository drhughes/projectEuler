# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 22:25:04 2018

@author: dave_
"""

#multiples of 3 or 5 sum below 1000
total = 0
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):       
        total += i
print(total)
