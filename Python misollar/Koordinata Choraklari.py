# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 21:28:20 2021

@author: User
"""

print("Koordinata o`qlarini kiriting, men choragini aytaman>>>")
x = float(input("x = >>"))
y = float(input("y = >>"))
 
if x > 0 and y >0:
    print("Birinchi chorakda")
elif x < 0 and y > 0:
    print("Ikkinchi chorak")
elif x < 0 and y < 0:
    print("Uchinchi chorak")
elif x > 0 and y < 0:
    print("To`rtinchi chorak")
elif x == 0 and y == 0:
    print("Koordinata Marazida joylashgan")
elif x == 0:
    print("X o`qining Nuqtasi")
elif x == 0:
    print("Y o`qining Nuqtasi")
    