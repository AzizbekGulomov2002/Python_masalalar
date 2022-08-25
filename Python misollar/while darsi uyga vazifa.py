# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:30:41 2021

@author: User
"""

# 73- masala
#(a va b natural sonlar berilgan. ularning EKUBi topilsin

"""a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a>b:
        a%= b
    else:
        b%= a
gcd = a + b
print(gcd)"""



#74- masala

"""n = int(input())
f1 = f2 = 1
print(f1, f2, end= " ")
i =2
while i<n:
    f1, f2 = f2, f1+f2
    print(f2, end= " ")
    i +=1"""


#75 - masala
def evklid(a,b):
    smail_num = a
    big_num = b
    end = True
    while end:
        if big_num%small_num == 0:
            end = False
            return small_num
        else:
            num = big_num%small_num
            big_num=small_num
            small_num=num
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    