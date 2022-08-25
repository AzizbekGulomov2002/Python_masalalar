# 6 - misol (Berilgan sonni Raqamlar yig`indisi va necha xonalik ekanini aniqlash)

def Digitcountsum(a):
    t=0
    s=0
    
    if 9<a and 100>a:
        n="Raqamlar soni: 2 ta"+"    Raqamlar yig'indisi: "+str(a//10+a%10)
    elif 0<a and a<10:
        n="Raqamlar soni: 1 ta      Raqamlar yig'indisi: "+str(a%10)
    elif 99<a and a<1000:
        n="Raqamlar soni: 3 ta      Raqamlar yig'indisi: "+str((a//10)//10+(a//10)%10+a%10)
  
        
    while a!=0:
        s+=a%10
        a=a//10
        t+=1
        
        
    return s,t
while (1):
    b=int(input("istalgan Sonni kiriting>>>"))
    print(Digitcountsum(b))
