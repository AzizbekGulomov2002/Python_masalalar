# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:57:48 2021

@author: User
"""

class Futbol:
    def __init__(self,*fut):
        
        self.fut1 = fut[0][0]
        self.fut2 = fut[0][1]
        
    def sarala(self):
        if int(self.fut1[1])*3 + int(self.fut1[2])>int(self.fut2[1])*3 + int(self.fut2[2]):
            print(self. fut1[0], "Mutlaq g`olib")
        elif int(self.fut1[1])*3 + int(self.fut1[2])< int(self.fut2[1])*3+int(self.fut2[2]):
            print(self.fut2[0],"mutlaq g`olib")
        else: 
            if int(self.fut1[4])>int(self.fut2[4]):
                print(self.fut1[0],"Mutlaq g`olib")
            elif int(self.fut1[4])<int(self.fut2[4]): 
                print(self.fut2[0],"Mutlaq g`olib")
            else:
                print("Durrang bo`ldi")
jamoa = [[],[]]          
a = input("Birinchi jamoa nomini kiriting: ")
jamoa[0].append(a)
b = input("Jamoaning g`alabalar sonini kiriting: ")
jamoa[0].append(b)
c = input("Jamoaning durrang sonini kiriting: ")
jamoa[0].append(c)
d = input("Jamoaning mag`lubiyat sonini kiriting: ")
jamoa[0].append(d)
e = input("Jamoaning gollar sonini kiriting: ")
jamoa[0].append(e)

          
a = input("Ikkinchi jamoa nomini kiriting: ")
jamoa[1].append(a)
b = input("Jamoaning g`alabalar sonini kiriting: ")
jamoa[1].append(b)
c = input("Jamoaning durrang sonini kiriting: ")
jamoa[1].append(c)
d = input("Jamoaning mag`lubiyat sonini kiriting: ")
jamoa[1].append(d)
e = input("Jamoaning gollar sonini kiriting: ")
jamoa[1].append(e)


    
futbol = Futbol(jamoa)
futbol.sarala()