# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:35:29 2021

@author: User
"""

class Odam:
    def __init__(self,name):
        self.name = name
        self.__age = 21
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,yosh):
        if yosh>0:
            self.__age = yosh
        else:
            print("yoshni qayta kiriting")
    def MalumotBer(self):
        print(self.name, "ning yoshi", self.__age, "da")
        
odam = Odam("Mirjalol")
odam.MalumotBer()

odam.age = 10
odam.MalumotBer()
a = odam.age

