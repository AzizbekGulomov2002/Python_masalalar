# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 20:43:04 2021

@author: User
"""


#Futbol o`yini

import random 
a = input("qaysi tarafga tepasiz====???")
b = ["chap", "o`ng", "o`rta"]
c = random.choice(b)
print(f"darvozabon {c} ga otildi")
if a == c:
    print("seyf")
else:
    print("<<<<gool>>>>")



