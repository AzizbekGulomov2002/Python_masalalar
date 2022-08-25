# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:15:09 2021

@author: User
"""
#Berilgan oraliqdagi sonning kvadrat bo`lganini ko`rsatadi

def Darajasini(x):
    d = 0
    for i in range(int(x/2)+1):
        if i*i == x:
            d = 1
    return d               
b=[]
for i in range(10):
    a = int(input("Sonni kiriting>>"))
    
    if Darajasini(a)==1:
        b.append(a)
print(b)








