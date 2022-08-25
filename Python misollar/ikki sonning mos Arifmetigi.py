# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:24:16 2021

@author: User
"""
#Sonlarni qaysi amalani tanlash orqali mos arifmetika
while True:
    a = float(input("Birinchi sonni Kiriting:>>"))
    work = input("Enter work (-+/*): ")
    b = float(input("Ikkinchi sonni kiriting>>>"))
    if work == "+":print(a,work,b, "=", a+b)
    elif work == "-":print(a,work,b, "=", a-b)
    elif work == "-":print(a,work,b, "=", a*b)
    elif work == "-":print(a,work,b, "=", a/b)



