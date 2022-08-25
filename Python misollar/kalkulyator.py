# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:11:00 2021

@author: User
"""

while True:
    print("1. Addition")
    print("2. Subtrction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choise = int(input("Enter your choice:"))
    if (choice>=1 and choise<=4):
        print("Enter two numbers:")
        num1 = int(input())
        num2 = int(input())
        if choice == 1:
            res = num1 + num2
            print("Result =", res)
        elif choise == 2:
            res = num1 - num2
            print("Result =", res)
        elif choice == 3:
            res = num1 * num2
            print("Result =", res)
        else:
            res = num1 / num2
            print("Result =", res)
    elif choice == 5:
        break
    else:
        print("Wrong input...!!!")