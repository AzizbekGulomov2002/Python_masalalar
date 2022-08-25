


#5 Berilgan koorinata orqali yuza va perimetr topish

x1=int(input("x1 ni kiriting>>"))
x2=int(input("y1 ni kiriting>>"))
y1=int(input("x2 ni kiriting>>"))
y2=int(input("y2 ni kiriting>>"))
def RectPS(x1,x2,y1,y2):
    s=(x2-x1)*(y2-y1)
    p=((x2-x1)+(y2-y1))*2
    return s,p
print(RectPS(x1,x2,y1,y2))
