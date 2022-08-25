# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:17:47 2021

@author: User
"""

class Odam():
    def __init__(self,ism,yosh):
        self.ism = ism
        self.yosh = yosh
    def malumotnoma(self):
        print(self.ism,self.yosh, "da")
class Talaba(Odam):
    def __init__(self,ism,yosh,universitet):
        Odam.__init__(self,ism,yosh)
        self.universitet = universitet
    def malumotnoma(self):
        super().malumotnoma()
        print(self.ism +self.universitet+ "da o`qiydi")
class Xaridor(Odam):
    def __init__(self,ism,yosh,xarid):
        super().__init__(ism, yosh)
        self.xarid = xarid
        
    def malumotnoma(self):
        print(self.ism + self.xarid + " sotib oldi ")
    def __str__(self):
        return("salim obyekti Xaridor Sinfini")
odamlar = [Odam("Ma`mura","25"),Talaba("Nosir","18", " Qarshi Davlat Universiteti"),Xaridor(" Mamur ","30"," Kitob ")]


odamlar[0].malumotnoma()
odamlar[1].malumotnoma()
odamlar[2].malumotnoma()

salim = Xaridor("Salim","26", " go`sht")
if isinstance(salim,Xaridor):
    print(" bu to`g`ri ")
    salim.malumotnoma()

else: 
    print("xato")