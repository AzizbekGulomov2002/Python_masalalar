
# While sikli kodlar blokini cheksiz takrorlash uchun ishlatiladi.
# Masalan, biz bir nechta foydalanuvchi yozuvlarini qayta ishlashimiz kerak, shunda foydalanuvchi har safar biror ma'lumotni kiritganida bir xil kod bloki bajariladi

# ism = input('Ismingiz nima ?')
# savol = f'Salom, {ism.title()}. Yoshinggizni ayting ?'
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yinggiz qancha ?")
# height = float(height)

#Bu bir martalik ishlatiladigan dastur



#while bu - toki degani
# son = 1
# while son<=5:
#     print(son, end=' ')
#     son+=1
    
#+1 ning ma'nosi har biriga 1ni qo'shib ketaver(1tadan oshib borayersin)



# print("Kiritilgan sonning kvadratlarini qaytaruvchi dastur")
# savol = "Istalgan sonni kiriting"
# savol+="(Dasturni to'xtatish uchun 'exit' deb yozing)"
# qiymat = ' ' #Qiymat matni bu - bo'sh matn
# while qiymat != 'exit': #Qiymat ichi bo'sh bo'lgani uchun qiymat kiritishni so'raydi
#     qiymat = input(savol) #Qiymatni o'zgaruvchiga yuklaydi
#     if qiymat != 'exit': #!= ning ma'nosi teng bo'lmasa degani
#         print(float(qiymat)**2) #Qiymatning kvadratini topib beradi



#break orqali ishlatilishi


# print("Kiritilgan sonni kvadratini aniqlovchi dastur")
# savol = "Istalgan sonni kiriting "
# savol+= "(Dasturni to'xtatmoqchi bo'lsanggiz exit deb yozing)"

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)


#for orqali bog'lanish


# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 6: #1dan 11gacha bo'lgan oraliqni ichidan 6gacha bo'lganini olgin deyildi
#         break
#     print (f'{son} ning kvadrati {son**2} ga teng')


#Sonlarni juft toqligini tekshirish
son = 0
while son<10:
    son+=1 #agar shuni olib tashlab run qilsa, abadiy sikl bo'lib qoladi
    if son%2!=0:
        continue
    else:
        print(son)
