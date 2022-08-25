# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:10:16 2021

@author: User
"""


"""import math
for i in range(11,100,2):
    print(math.pow(i,3))"""
    
    
#Raqamlar yig`indisi    
"""a = int(input("a sonni kiriting!"))
b = int(input("b sonni kiriting!"))
t = 0
if a>b:
    print("Dasturni qaytadan kiriting!")
else:
    for i in range(a, b+1 ,1):
        t+=i
        print(i)
    print(t)
    print(f"Sonlar yig`indisi {t} ga teng!")"""



#Raqamlar Faktoriali
import math
a = int(input("a sonni kiriting!"))
b = int(input("b sonni kiriting!"))
t = 0
if a>b:
    print("Sonlarni qaytadan kiriting!")
else:
    for i in range(a, b+1 ,1):
        t+=math.factorial(i)
        print(i)
    print(t)
    print(f"Sonlar faktoriyali {t} ga teng!")
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    