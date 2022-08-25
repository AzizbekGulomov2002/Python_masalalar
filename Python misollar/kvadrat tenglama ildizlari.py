# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 21:06:57 2021

@author: User
"""

#kvadrat tenglama ildizlari


a = float(input("tenglamaning a koefitsentini kiriting>>>"))
b = float(input("tenglamaning b kofitsentini kiriting>>>"))
c = float(input("tenglamaning c koefitsentini kiriting>>>"))
D = (b * b) - (4 * a * c)
print(D)
if D>0:
    x1 = (-b + sqrt(D))/(2 * a)
    x2 = (-b - sqrt(D))/(2 * a)
    print(x1, x2)
elif D == 0:
    x = -b/(a * 2)
    print(x)
else:
    print("tenglama yechimga ega emas!!!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    