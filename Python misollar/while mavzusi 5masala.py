# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:10:29 2021

@author: User
"""

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
            