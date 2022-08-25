# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:11:28 2021

@author: User
"""

#To`g`ri Burchakli uchburchakning barcha o`lchamlari


import math 
AB = input("Birinchi katet uzunligini kiriting>>>")
AC = input("Ikkinchi katet uzunligini kiriting>>>")

AB = float(AB)
AC = float(AB)

BC = math.sqrt(AB ** 2 + AC ** 2)

S = (AB * AC)/2
P = AB + AC + BC

print("Uchburchak Yuzasi: %.2f" % S)
print("Uchburchak Perimetri: %.2f" % P)