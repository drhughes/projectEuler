# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 22:49:28 2018

@author: dave_
"""
fib = [1, 2]
i = 0
ans = 0
while True:    
    fib.append(fib[i] + fib[i+1])
    i=i+1
    if fib[i]<4000000:
        if fib[i] % 2 ==0:
            ans = ans + fib[i]
    else:
        break
        
print(ans)
