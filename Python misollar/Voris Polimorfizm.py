# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 01:41:47 2021

@author: User
"""

#Vorislik - Bir class dan boshqa bir class yaratish

class Shaxs:
    "Shaxslar haqida ma`lumot"
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport},{self.familiya}"
        return info
    def get_age(self,yil):
        return yil - self.tyil
class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosich. ID raqami: :{self.idraqam}"
        return info
class Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    def get_manzil(self):
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko`chasi, {self.uy}- uy"
        return manzil
talaba1_manzil = Manzil(12,"Olmazor","Qarshi","Dubay")
talaba1 = Talaba("Valijon","aliyev","FA1229898",2002,"0292929",talaba1_manzil)
talaba1.manzil.get_manzil()
    
#Polimarfizm


    
        