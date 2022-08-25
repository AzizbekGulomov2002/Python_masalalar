# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:00:04 2021

@author: User
"""

#Berilgan sonni teskarisini Topish

n1 = int(input("Biror son kiriting>>>"))
n2 = 0
while n1>0:
    digit = n1%10
    n1 = n1//10
    n2 = n2 * 10
    n2 = n2 + digit
print("Teskarisi >>>" , n2)
