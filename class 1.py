# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:33:18 2021

@author: User
"""
#Exception - Istisno
"""try:
    print(int("12"))
except:
    print("Xatolik")
finally:
    print("Dastur tamom")"""
    
    
class MashinaSinfi:
    modeli = "Gentra"
    otkuchi = "90"
    rangi = "sariq"
    yili = "1996"
    def moshinahaqida(self):
        print(self.modeli, "mashinasining ot kuchi" ,self.otkuchi, "ga teng")
    def moshinarangihaqida(self):
        print(self.modeli, "mashinasining rangi" ,self.rangi,"ga bo`yalgan")    

     
gentra = MashinaSinfi()
gentra.rangi = "matviy"
gentra.moshinarangihaqida()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        