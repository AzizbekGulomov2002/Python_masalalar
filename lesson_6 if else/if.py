# Shart operatorlari

#Biror shartni bajarish uchun foydalanishimiz mumkin bo'lgan barcha kalit so'zlardan iborat va barcha dasturlash tillarida ishlatiladigan shart oerator turkumidir.

#Shart operatorlari - 3turga bo'linadi (1-if, 2-elif, 3-else)


# x = 22;
# if x == 22:
#     print('x soni bir biriga teng')
    
# elif x < 22:
#     print('x 22 sonidan kichik')

# else:
#     print('Ikkala shartni ham qanoatlantirmaydi :(')


#Sonlarni taqqoslash

# a = int(input("birinchi sonni kiriting, men taqqoslayman = "))
# b = int(input("ikkinchi sonni kiriting, men taqqoslayman = "))

# if a == b:
#     print("Ushbu sonlar bir biriga teng ekan")
# elif a>b:
#     print(a, "soni ", b, "sonidan katta ekan")
# else:
#     print(a,"soni ", b, "sonidan kichik ekan")

#Shart operatorlaridan biriga bir nechta qiymatlarni (and kalit so'zi orqali) berib ketish mumkin
#uchburchakning arametrlariga doir masala

# a = float(input("Uchburchakning birinchi tomonini kiriting :"))
# b = float(input("Uchburchakning ikkinchi tomonini kiriting :"))
# c = float(input("Uchburchakning uchinchi tomonini kiriting :"))

# if a+b>c and a+c>b and b+c>a:
#     print("Demak uchburchak yasash mumkin ekan ")
# else:
#     print("Bu tomonlardan uchburchak bo'lmaydi !!!!! ")

# if a==b==c:
#     print("Teng tomonli Muntazam uchburchak bo'lar ekan")
    

# if a==b or b==c:
#     print("Bu uchburchak teng yonli ekan") 




#Sonlarning maxmimum va minimum qiymatlarini topish
#a = 5, b=4, c=3

# a = float(input(" birinchi tomonini kiriting :"))
# b = float(input(" ikkinchi tomonini kiriting :"))
# c = float(input(" uchinchi tomonini kiriting :"))

# if a>=b and b>=c:
#     print(f"eng katta son + {a}!")
    
# if a == b and b == c:
#     print("Bu sonlar bir xil")
    
# if a<=b and b<=c:
#     print(f"eng katta son + {c}!")
    
# if b>=a and a>=c:
#     print(f"eng katta son + {b}!")


#uchburchakning diskriminant qiymatini topish



# a = float(input("Uchburchakning birinchi tomonini kiriting :"))
# b = float(input("Uchburchakning ikkinchi tomonini kiriting :"))
# c = float(input("Uchburchakning uchinchi tomonini kiriting :"))

# D = b**2 - 4*a*c

# if D>0:
#    print("Sonninng qiymati 0 dan kichik") 
   
# elif D<0:
#     print("Sonninng qiymati 0 dan katta") 

# else:
#    print("Sonninng qiymati 0 ga teng") 