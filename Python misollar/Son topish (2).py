# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 20:56:22 2021

@author: User
"""

from random import randrange
oylanganSon = randrange(1000,10000,1)
kiritilganSon = int(input("Men o'ylagan son nechchi deb o'ylaysiz:>>>"))
for i in range(1,15,1):
    if oylanganSon==kiritilganSon:
        print("Tabriklaymiz. Siz yutdingiz!")
        break
    elif oylanganSon<kiritilganSon:
        print("Bu soningiz o'ylangan sondan katta.")
        kiritilganSon = int(input("Man o'ylagan son nechchi deb o'ylaysiz:>>>"))
    elif oylanganSon>kiritilganSon:
        print("Bu soningiz o'ylangan sondan kichik.")
        kiritilganSon = int(input("Man o'ylagan son nechchi deb o'ylaysiz:>>>"))

else:
    print("Yutqazdingiz.")














