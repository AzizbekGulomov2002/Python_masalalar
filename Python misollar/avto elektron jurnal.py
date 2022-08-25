# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:21:29 2021

@author: User
"""

class Haydovchi():
    def __init__(self,ism,familiyasi,rusumi,avtoraqam):
        self.ism = ism
        self.familiyasi = familiyasi
        self.rusumi = rusumi
        self.avtoraqam = avtoraqam
    @property
    def ism(self):
        return self.__ism
    @ism.setter
    def ism(self,ism):
        if len(ism)>2:
            self.__ism = ism
        else: 
            raise Exception("Ism 3ta harfdan ko`p bo`lishi kerak!")
            
    @property
    def familiya(self):
        return self.__familiya
    @familiya.setter
    def familiya(self,familiyasi):
        if len(familiyasi)>2:
            self.__familiyasi = familiyasi
        else:
            raise Exception("Familiya 3ta harfdan ko`p bo`lishi kerak!!")
            
    @property
    def rusumi(self):
        return self.__rusumi
    @rusumi.setter 
    def rusumi(self,rusumi):
        if len(rusumi)>2:
            self.__rusumi = rusumi
        else:
            raise Exception("Rusumi 3ta harfdan ko`p bo`lsin!!")
            
    @property
    def avtoraqam(self):
        return self._avtoraqam
    @avtoraqam.setter
    def avtoraqam(self,avtoraqam):
        if len(avtoraqam)>2:
            self._avtoraqam = avtoraqam
        else:
            raise Exception("Avtoraqam 3tadan oshmasin!!")
class Haydovchilar:
    haydovchi = [
        Haydovchi("ism","familiya","rusumi","avtoraqam")
        ]
    def haydovchi_qushish(self):
        print("yangi Haydovchi qo`shish")
        ism = input("ismini kiriting:")
        familiya = input("familiyasini kiriting:")
        rusumi = input("Mashina Rusumini kiriting:")
        avtoraqam = input("Avtoraqamni kiriting:")
        self.haydovchi.append(Haydovchi(ism,familiya,rusumi,avtoraqam))
    def chiqarish(self):
        print("O`rni|","ism|","familiya","rusumi","avtoraqam")
        for index,i in enumerate(self.haydovchi,start = 1):
            print(index,"|",i.ism,"|",i.familiya,"|",i.rusumi,"|",i.avtoraqam)
    def uchirish(self):
        while True:
            self.chiqarish()
            try:
                m = int(input("O`chirmoqchi bo`lgan obyektni o`rnini kiriting!"))
                if m>=0 and m<len(self.haydovchi):
                    self.haydovchi.pop(self.haydovchi[int(m)])
                    self.chiqarish()
                else:
                    print('Qaytadan kiritib ko\'ring o`rin kiritishda xatolik')
                
         
            
            
            except:
                print('Siz raqam kiritmadiz. E\'tiborli bo\'ling')
                m = input('Amalni to`xtatmoqchimisiz: (1/0): ')
            if  m=='1':
         
         
                break
    def saralash(self):
        m = input("Qaysi nom bo'yicha saralamoqchisiz? ")
        if m=='ism':
            self.haydovchi.sort(key=lambda x: x.ism)
        elif m=='familiya':
            self.haydovchi.sort(key=lambda x: x.familiya)
        elif m=='rusum':
            self.haydovchi.sort(key=lambda x: x.rusumi)
        elif m == "avtoraqam":
            self.haydovchi.sort(key=lambda x: x.avtoraqam)
        else:
            print('xato qaytadan urinib ko\'ring. ') 
            
    def izlash(self):
        m = input("avtomobil rusumini kiriting")
        n = input("avtomobil raqamini kiriting")
        for i in self.haydovchi:            
            if (m in i.rusumi) and (n in i.avtoraqam):
                print(i.ism,i.familiya,i.rusumi,i.avtoraqam)
                
avto = Haydovchilar()
while True :
    m = input("Qaysi amalni tanlaysiz.Raqamlara kiriting:1-chiqarish.2-qo`shish.3-izlash.0-chiqish:")
    if m == "1":
        avto.chiqarish()
    elif m == "2":
        avto.qushish()
    elif m == "3":
        avto.izlash()
    elif m == "0":
        break
        
            

            
            
            
            
            
            
            
            
            
            