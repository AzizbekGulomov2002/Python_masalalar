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
"""import math
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
    print(f"Sonlar faktoriyali {t} ga teng!")"""
    
    
"""import math
t = 0
    
for i in range(1,28,1):
    t+=(i**2 + 2*i)/(i**3 + i*math.cos(i)**2 + 1)
print(t)"""

    

t = 1
for i in range(1,21,1):
    t*=(i**2 + 1)/((i**3)**(1/i) + 2)
print(t)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    