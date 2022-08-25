#7 - misol. Berilgan sonning teskarisini topish

def InvertDigits(a):
    if 9<a and 100>a:
        n=str(a%10)+str(a//10)
    elif 0<a and a<10:
        n=str(a%10)
    elif 99<a and a<1000:
        n=str(a%10)+str((a//10)%10)+str((a//10)//10)
    else:
        n="Xato oraliq. Kichikroq son kiriting"
    return n
while (1):
    b=int(input("Son kiriting: "))
    print(InvertDigits(b))
