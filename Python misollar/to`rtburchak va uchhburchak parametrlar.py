# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:50:37 2021

@author: User
"""
#To`g`ri buechakli uchburchak yuzasi va perimetri 


"""import math
AB = input("Birinchi katetni kiriting>>>")
AC = input("Ikkinchi katetni kiriting>>>")
AB = float(AB)
AC = float(AC)

BC = math.sqrt(AB ** 2 + AC ** 2)

S = (AB * AC)/2
P = AB + AC + BC
print("Uchburchak yuzasi == %.2f" % S)

print("Uchburchak perimetri == %.2f" %P)"""


from math import sqrt
a = float(input("a sonni kiriting>>> ="))
b = float(input("b sonni kiriting>>>="))
c = float(input("c sonni kiriting>>>="))

d = b * b - 4 * a * c
if d > 0:
    x1 = (-b + sqrt(d))/(2 * a)
    x2 = (-b - sqrt(d))/(2 * a)
    print("x1 = %; x2 = %.2f" % (x1, x2))
elif d == 0:
    x1 = -b/(2 * a)
    print("x1 = %.2f" % x1)
else:
    print("Ildizlari mavjud emas")
    











