# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 16:42:50 2021

@author: User
"""

n = int(input("Nechta element bo`lsin>>>>"))
a = []
b = []
c = []
d = []
for i in range(n):
   a.append(int(input("A elementni kiriting>>")))

for i in range(n):
  
    
    if a[i]%2 == 0:
        b.append(a[i])
print(len(b),b)






