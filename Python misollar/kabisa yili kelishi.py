# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 22:00:33 2021

@author: User
"""

   #Kabisa yili kelishi     

a = int(input("Ixtiyoriy yilni ayting, men kabisa yoki yo`qligini aniqlayman!==>"))
if (a%400 == 0 or (a%100 != 0 and a%4==0)):
    print("Bu Kabisa yili")
else:
    print("Afsus Bu yil Kabisa yili Emas!!!")
    