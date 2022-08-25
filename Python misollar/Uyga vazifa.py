# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 04:09:06 2021

@author: User
"""

class Kutubxona():
    def __init__(self,kitobnomi,muallif,nashiryot,yil):
        self.kitobnomi = kitobnomi
        self.muallif = muallif
        self.nashiryot = nashiryot
        self.yil= yil
    @property
    def kitobnomi(self):
        return self.__kitobnomi
    @kitobnomi.setter
    def kitobnomi(self,kitobnomi):
        if len(kitobnomi)>2:
            self.__kitobnomi = kitobnomi
        else: 
            raise Exception("Kitobnomi 3ta harfdan uzun bo`lsin")
            
    @property
    def muallif(self):
        return self.__muallif 
    @muallif.setter 
    def muallif(self,muallif):
        if len(muallif)>2:
            self.__muallif = muallif
        else:
            raise Exception("Muallif ismi 2harfdan uzun bo`lsin")
            
    @property
    def nashiryot(self):
        return self.__nashiryot
    @nashiryot.setter
    def nashiryot(self,nashiryot):
        if len(nashiryot)>2:
            self.__nashiryot = nashiryot
        else:
            raise Exception("nashiryot nomi 2ta harfdan kop bo`lsin")
            
            
    @property
    def yil(self):
        return self.__yil
    @yil.setter 
    def yil(self,yil):
        if len(yil)>2:
            self.__yil = yil
        else:
            raise Exception("Yilni uzunroq yozing")
        
class Kutubxona_guruhi:
    Ruyhatlar = [
        Kutubxona("kitob nomi","muallif","nashiryot","yil",)
        ]
    
    
    
    def Kutubxona_qushish(self):
        print('Yangi kitob qo`shish:')
        kitobnomi = input('Kitob nomini kiriting:> ')
        muallif = input('Muallifni kiriting> ')
        nashiryot = input('Nashiryot nomini kiriting> ')
        yil = input("Yilni kiriting: >")
        self.Ruyhatlar.append(Kutubxona(kitobnomi,muallif,nashiryot,yil))  
    
    def chiqarish(self):
        print('O`rni|','kitob nomi|','Muallif|','Nashiryot|',"Ishlangan Yili")
        for index,i in enumerate(self.Ruyhatlar,start=0):
            print(index,'|', i.kitobnomi,'|',i.muallif,'|',i.nashiryot, "|",i.yil)

    def uchirish(self):
        while True:
                
            self.chiqarish()
           
            m = int(input("O'chirmoqchi bo'lgan Kitobni  kiriting: "))
            print(type(m))
            if m>=0 and m<len(self.Ruyhatlar):
                self.Ruyhatlar.remove(self.Ruyhatlar[int(m)])
                self.chiqarish()
            else:
                print('Qaytadan kiritib ko\'ring  kiritishda xatolik')
                
            
            
            m = input('Amalni to`xtatmoqchimisiz: (1/0): ')

            if m=='1':
                break
        

    def saralash(self):
        m = input("Qaysi nom bo'yicha saralamoqchisiz? ")
        if m=='kitobnomi':
            self.Kutubxona.sort(key=lambda x: x.kitobnomi)
        elif m=='muallif':
            self.Kutubxona.sort(key=lambda x: x.muallif)
        elif m == "nashiryot":
            self.Kutubxona.sort(key=lambda x: x.nashiryot)
        elif m=='yil':
            self.Kutubxona.sort(key=lambda x: x.yil)
        else:
            print('xato qaytadan urinib ko\'ring. ')
            
    def izlash(self):
        m = input("Qidirmoqchi bo`lgan Kitobni kiriting :")
        n = input("Muallif ismini kiriting :")
        for i in self.Ruyhatlar:
            if (m in i.kitobnomi) and (n in i.muallif):
                print(i.kitobnomi,i.muallif)


    
tg = Kutubxona_guruhi()
while True:

    m = input('Amalni tanlang:(1-chiqarish, 2-qushish,3-o\'chirish,4-saralash,5-izlash, 0-dasturdan chiqish):> ')

    if m=='1':
        tg.chiqarish()
    elif m=='2':
        tg.Kutubxona_qushish()
    elif m=='0':
        break
    elif m=='4':
        tg.saralash()
    elif m=='3':
        tg.uchirish()
    elif m == "5":
        tg.izlash()















    
        
        
        
        
        
        
        