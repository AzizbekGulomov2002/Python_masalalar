#while bu - siklli kodlar blokini cheksiz ko'rinishda takrorlash uchun ishlatiladi.

#masalan - biz bir nechta foydalanuvchi yozuvlarini qayta ishlashimiz kerak, shunda foydalanuchi har safar biror ma'lumotni kiritganida bir xil javobni oladi.

# ism = input("Isminggiz nima ?")
# savol = f'Salom, hurmatli {ism.title()}. Yoshinggiz nechada ?'
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yinggiz qancha ?")
# height = float(height)


#while - toooki manashu qiymat qanoatlanmaguncha ishlayversin.

# son = 1 #son 1dan boshlansin degani
# while son<=11: #toki 5gacha bo'lgan sonni 
#     print(son, end=' ') #chiqarib bersin 
#     son+=2 #va har biria 1 qo'shib ketsin
    
#ma'nosi 5gacha bo'lgan sonlarning har biriga 1ni qo'shib ketaversin


# print("Kiritilgan sonnni kvadratini aniqlovchi dastur")
# savol = "Istalgan sonni kirting"
# savol+=("Dasturni tugatish uchun exit yozuvini yozing")
# qiymat = ' '
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)




#break bilan bog'lanish

# print("Kiritilgan sonnni kvadratini aniqlovchi dastur")
# savol = "\Istalgan sonni kiriting"
# savol+="(Dasturni to'xtatish uchun (exit) yozuvini yozing)"


# while True: #Toki kiritilgan qiymatng savol o'zgaruvchisi qabul qilinsa
#     qiymat = input(savol)
#     if qiymat == 'exit': #exit buyrug'ini bersa
#         break #Dastur to'liq to'xtatilsin
#     else: #Aks holda, ya'ni exit bermasa, ishlab qiymatni chiqaraversin 
#         print(float(qiymat)**2)




# sonlar = list(range(1,6))
# for son in sonlar:
#     if son == 2: #ro'yxat ichidagi oraliqdan 7gacha bo'lganini hisoblasin va 7dan keyingisi break qilib amalga oshirmasin !
#         break
#     print(f'{son} ning kubi {son**3} ga teng')



# son = 0
# while son<10:
#     son+=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)