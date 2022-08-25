# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:19:07 2021

@author: User
"""

import random
n = 100
numbers = list(range(1,n+1))
x = numbers.pop(random.randint(1,n+1))
print(x)

summa = n*(n+1)/2
print(summa - sum(numbers))