# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 21:53:25 2021

@author: User
"""

# Hafta kunlarini qaysi raqamdaligini aniqlash



#Hafta kunlari Raqam bilan

"""a = int(input(f"Hafta kunini kiriting!>>>"))
if a == 1:
    print("Bu Dushanba kuni")
elif a == 2:
    print("Bu Seshanba kuni")
elif a == 3:
    print("Bu Sheshanba kuni")
elif a == 4:
    print("Bu Chorshanba kuni")
elif a == 5:
    print("B Juma kuni")
elif a == 6:
    print("Bu Shanba kuni")
elif a == 7:
    print("Bu Yakshanba kuni")
else:
    print("Boshqatdan Kiriting!!")    """




                

from random import randrage 
oylanganSon = randrage (100,1000,1)
print(oylanganSon)
kiritilganSon = int(input("Men o`ylagan son bundan kattaroq"))
for i in range(1,15,i):
    if oylanganSon == kiritilganSon:
      print("Tabriklaymiz, yutdingiz")
      break
    elif oylanganSon<kiritilganSon:
      print("Kiritgan soningiz o`ylangan sondan katta")
else:
    print("Yutqazdingiz")



















    