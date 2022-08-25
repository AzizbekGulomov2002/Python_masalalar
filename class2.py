# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:11:07 2021

@author: User
"""

"""class Odam:
    ismi = "Azizbek"
    yosh = "18"
    malumoti = "O`rta"
    manzil = "Qarshi"
    def Odamhaqida(self):
        print(self.ismi, "G`ulomov" ,self.yosh, "da")
    def Odamhaqida(self):
        print(self.ismi, "G`ulomov" ,self.manzil, "shahar")
        


manzil = Odam()
manzil.manzil = "QARSHI"
manzil.Odamhaqida()"""



class Odam:
    def __init__(self,ismi, familia, yoshi, malumoti):
        self.ismi = ismi
        self.familia = familia
        self.yoshi = yoshi
        self.malumoti = malumoti
        
    def Odamhaqida(self,qiziqishi):
        print(self.ismi, self.familia,qiziqishi,"qiziqadi")
kamronbek = Odam("Kamronbek", "Holmirzayev", 5, "yo`q")
kamronbek.Odamhaqida("moshinaga")






















